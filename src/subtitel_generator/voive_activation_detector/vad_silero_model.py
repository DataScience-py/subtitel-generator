"""
Voice activation detection module.

Use silero-vad for voice activation detection module.

Thanks snakers4 for the silero-vad library.
https://github.com/snakers4/silero-vad
"""

from pathlib import Path

from silero_vad import get_speech_timestamps, load_silero_vad, read_audio

from subtitel_generator.logger import get_logger
from subtitel_generator.subtitel_model import Subtitels

from .base import BaseVAD


class VADSilero(BaseVAD):
    """Silero-vad class for speech detection."""

    def __init__(self) -> None:
        """__init__ load silero-vad model."""
        self.logger = get_logger("SileroVad")
        self.model = load_silero_vad()

    def detect(self, audio_file_path: str | Path) -> list[Subtitels]:
        """
        Detect speech in audio file.

        Parameters
        ----------
        audio_file_path : str | Path
            path to audio file, when need generate vad result.

        Returns
        -------
        list[Subtitels]
            list of times, when have speech.
        """
        wav = read_audio(audio_file_path)
        speeches = get_speech_timestamps(
            wav,
            self.model,
            return_seconds=True,
        )

        result: list[Subtitels] = []
        for speech in speeches:
            result.append(
                Subtitels(
                    start=speech["start"],
                    end=speech["end"],
                    text="",
                    target="",
                )
            )

        return result
