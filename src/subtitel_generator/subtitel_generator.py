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

from .voive_activation_detector import BaseVAD


class SubtitelGenerator:
    """Class when generate subtitels."""

    def __init__(self, vad: BaseVAD) -> None:
        """
        __init__ for the class.

        Parameters
        ----------
        vad : BaseVAD
            VoiceActivationDetection class.
        """
        self.vad = vad
