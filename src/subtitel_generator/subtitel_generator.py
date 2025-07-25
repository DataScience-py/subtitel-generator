"""Module for the Bsae class of the application.

Get some modules, when be important for the application.

- VoiceActivationDetection module for generate times, when need subtitels.
- SpeechToText module for generate text from voice. Use output from
VoiceActivationDetection module.
- Translater module for translate text.

Supported languages:
- en: English
- ru: Russian

Generate sub for russian user from english text.
"""

from pathlib import Path

from .speech_to_text import BaseSTT
from .subtitel_model import Subtitels
from .voive_activation_detector import BaseVAD


class SubtitelGenerator:
    """Class when generate subtitels."""

    def __init__(self, vad: BaseVAD, stt: BaseSTT) -> None:
        """
        __init__ for the class.

        Parameters
        ----------
        vad : BaseVAD
            VoiceActivationDetection class.
        """
        self.vad = vad
        self.stt = stt

    def vad_generate(self, audio_file: str | Path) -> list[Subtitels]:
        """Return output from vad models."""
        return self.vad.vad_detect(audio_file)

    def stt_generate(
        self, audio_file: str | Path, timesamps_speeches: list[Subtitels]
    ) -> list[Subtitels]:
        """Generate text for subtitel."""
        return self.stt.stt_generate(audio_file, timesamps_speeches)
