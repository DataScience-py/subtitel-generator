"""
Vosk model for STT.

You need install model when you need language.
See: https://alphacephei.com/vosk/models

"""

import io
import json
import os
import wave
from pathlib import Path

from pydub import AudioSegment
from vosk import KaldiRecognizer, Model

from subtitel_generator.subtitel_model import Subtitels, Timestamps
from subtitel_generator.utils.logger import get_logger

from .base import BaseSTT


class VoskSTT(BaseSTT):
    """Vosk model for STT."""

    def _path_to_model(self) -> str:
        """Path to model."""
        path = Path(__file__).parent.parent.parent.parent / "models" / "vosk"
        print(f"model path {path}")
        self.logger.debug(f"choice this model {os.listdir(path)}")
        return os.path.join(str(path), os.listdir(path)[0])

    def __init__(self) -> None:
        """Init Vosk model for STT."""
        self.logger = get_logger("VoskSTT")
        model_path = self._path_to_model()
        self.model = Model(model_path)
        self.wf: wave.Wave_read | None = None  # audio bytes

        self.frame_rate: int | None = None
        self.nframes: int | None = None

    def _convert_audio_to_mono_16bit(self, input_file: str | Path) -> None:
        """
        _convert_audio_to_mono_16bit.

        Parameters
        ----------
        input_file : str | Path
            file name
        """
        audio = AudioSegment.from_file(input_file)

        if audio.channels != 1:
            audio = audio.set_channels(1)
        if audio.sample_width != 2:
            audio = audio.set_sample_width(2)

        in_memory_file = io.BytesIO()

        audio.export(in_memory_file, format="wav")

        in_memory_file.seek(0)

        self.wf = wave.open(in_memory_file, "rb")

        input_file = Path(input_file)

        self.logger.debug(
            f"Audio file '{input_file.name}' converted to mono 16-bit PCM."
        )

    def _load_audio(self, audio_file: str | Path) -> None:
        """
        _load_audio.

        Parameters
        ----------
        audio_file : str | Path
            path to audio file.
        """
        audio_file = Path(audio_file)
        if self.wf:
            self.wf.close()

        self.wf = wave.open(str(audio_file), "rb")

        if (
            self.wf.getnchannels() != 1
            or self.wf.getsampwidth() != 2
            or self.wf.getcomptype() != "NONE"
        ):
            self.logger.warning(
                "Audio file must be mono, 16-bit PCM.\n Start recrate audio"
            )
            self.wf.close()
            self._convert_audio_to_mono_16bit(str(audio_file))

        self.frame_rate = self.wf.getframerate()
        self.nframes = self.wf.getnframes()
        self.logger.debug(
            f"Audio file'{audio_file.name}' loaded. "
            f"Frame rate: {self.frame_rate} Hertz (Hz), "
            f"All frames: {self.nframes}"
        )

    def _get_audio_segment_data(
        self, start_sec: float, end_sec: float
    ) -> bytes:
        """
        _get_audio_segment_data.

        Parameters
        ----------
        start_sec : float
            start seconds
        end_sec : float
            end seconds

        Returns
        -------
        bytes
            audio fragment

        Raises
        ------
        RuntimeError
            if audio file not loaded
        """
        if not self.wf or not self.frame_rate or not self.nframes:
            raise RuntimeError(
                "Audio file not loaded. Please load audio file first."
            )

        start_frame = int(start_sec * self.frame_rate)
        end_frame = int(end_sec * self.frame_rate)

        start_frame = max(0, start_frame)
        end_frame = min(self.nframes, end_frame)

        self.wf.setpos(start_frame)

        num_frames_to_read = end_frame - start_frame
        if num_frames_to_read <= 0:
            self.logger.warning(
                "readframes() returned 0 frames, returning empty bytes"
            )
            return b""

        return self.wf.readframes(num_frames_to_read)

    def generate(
        self,
        audio_file_path: str | Path,
        timestamps_speeches: list[Timestamps],
    ) -> list[Subtitels]:
        """
        Generate text from audio file.

        Parameters
        ----------
        audio_file_path : str | Path
            path to audio file
        timestamps_speeches : list[Timestamps]
            list of speeches, when need text

        Returns
        -------
        list[Subtitels]
            subtitels. Language is Video Subtitle.
        """
        try:
            self._load_audio(audio_file_path)

            subtitels: list[Subtitels] = []

            for i, segment in enumerate(timestamps_speeches):
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

                if recognized_text == "":
                    self.logger.warning(
                        "Text is empty. {segment_start:.2f}-{segment_end:.2f}s"
                    )

                subtitels.append(
                    Subtitels(
                        start=segment_start,
                        end=segment_end,
                        text=recognized_text,
                    )
                )
                self.logger.debug(
                    f"Segment {i + 1} {segment_start:.2f}-{segment_end:.2f}s:"
                    f"{recognized_text}"
                )

        finally:
            if self.wf:
                self.wf.close()
                self.wf = None
        return subtitels
