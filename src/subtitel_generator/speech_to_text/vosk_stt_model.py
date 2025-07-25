"""Vosk model for STT."""

import json
import wave
from pathlib import Path

from vosk import KaldiRecognizer, Model

from subtitel_generator.subtitel_model import Subtitels

from .base import BaseSTT


class VoskSTT(BaseSTT):
    """Vosk model for STT."""

    def __init__(self, model_path: str | Path) -> None:
        """Init Vosk model for STT."""
        self.model = Model(model_path)
        self.wf: wave.Wave_read | None = None

        self.frame_rate: int | None = None
        self.nframes: int | None = None

    def _load_audio(self, audio_file: str | Path) -> None:
        """Load audio file."""
        audio_file = Path(audio_file)
        if self.wf:
            self.wf.close()

        self.wf = wave.open(str(audio_file), "rb")

        if (
            self.wf.getnchannels() != 1
            or self.wf.getsampwidth() != 2
            or self.wf.getcomptype() != "NONE"
        ):
            raise ValueError("Audio file must be mono, 16-bit PCM.")

        self.frame_rate = self.wf.getframerate()
        self.nframes = self.wf.getnframes()
        print(
            f"Аудиофайл '{audio_file.name}' загружен. "
            f"Частота дискретизации: {self.frame_rate} Гц, "
            f"Всего фреймов: {self.nframes}"
        )

    def _get_audio_segment_data(
        self, start_sec: float, end_sec: float
    ) -> bytes:
        if not self.wf or not self.frame_rate or not self.nframes:
            raise RuntimeError(
                "Аудиофайл не загружен. Вызовите _load_audio_for_vosk сначала."
            )

        start_frame = int(start_sec * self.frame_rate)
        end_frame = int(end_sec * self.frame_rate)

        start_frame = max(0, start_frame)
        end_frame = min(self.nframes, end_frame)

        self.wf.setpos(start_frame)

        num_frames_to_read = end_frame - start_frame
        if num_frames_to_read <= 0:
            print("readframes() returned 0 frames, returning empty bytes")
            return b""

        return self.wf.readframes(num_frames_to_read)

    def stt_generate(
        self, audio_file: str | Path, timestamps_speech: list[Subtitels]
    ) -> list[Subtitels]:
        """STT generate for audio."""
        self._load_audio(audio_file)

        updated_timestamps_speech: list[Subtitels] = []

        for i, segment in enumerate(timestamps_speech):
            segment_start = segment["start"]
            segment_end = segment["end"]

            segment_audio_data = self._get_audio_segment_data(
                start_sec=segment_start, end_sec=segment_end
            )

            if not segment_audio_data:
                continue

            recognizer = KaldiRecognizer(self.model, self.frame_rate)
            recognizer.AcceptWaveform(segment_audio_data)

            result_json = recognizer.FinalResult()
            result = json.loads(result_json)

            recognized_text = result.get("text", "").strip()

            updated_timestamps_speech.append(
                Subtitels(
                    start=segment_start, end=segment_end, text=recognized_text
                )
            )
            print(
                f'Сегмент {i + 1} ({segment_start:.2f}-{segment_end:.2f}s): "{recognized_text}"'
            )

        # Закрываем аудиофайл после обработки всех сегментов
        if self.wf:
            self.wf.close()
            self.wf = None
        print(updated_timestamps_speech)
        return updated_timestamps_speech
