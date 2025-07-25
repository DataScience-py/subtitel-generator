"""
Voice activation detection module.

Use vosk-vad model to detect voice activation.
"""

from pathlib import Path

from silero_vad import get_speech_timestamps, load_silero_vad, read_audio

from subtitel_generator.subtitel_model import Subtitels

from .base import BaseVAD


class VADSileroDetector(BaseVAD):
    """Vosk voice activation detection module."""

    def __init__(self) -> None:
        """Initialize silero model for vad."""
        self.model = load_silero_vad()

    def vad_detect(self, audio_file: str | Path) -> list[Subtitels]:
        """
        vad_detect List of speech results.

        Parameters
        ----------
        audio : str | Path
            path to audio file

        Returns
        -------
        list[SppechingResult]
            List of speech results
        """
        # TODO: remove this print and use logger
        print("START SPEECH")
        wav = read_audio(audio_file)
        speeches = get_speech_timestamps(
            wav,
            self.model,
            return_seconds=True,
        )
        print(f"{speeches=}")

        result: list[Subtitels] = []
        for speech in speeches:
            print(f"{speech=}")
            result.append(
                Subtitels(start=speech["start"], end=speech["end"], text="")
            )

        return result
