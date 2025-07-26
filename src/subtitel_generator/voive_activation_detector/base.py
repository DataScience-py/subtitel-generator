"""
Base VAD class for voice activation detection.

This class is an abstract base class for voice activation detection.
It defines theinterface for subclasses to implement the detection logic.
"""

from abc import ABC, abstractmethod
from pathlib import Path

from subtitel_generator.subtitel_model import Subtitels


class BaseVAD(ABC):
    """Base Voice Activation Detection class (Abstract Base Class)."""

    @abstractmethod
    def detect(self, audio_file_path: str | Path) -> list[Subtitels]:
        """
        Generate list speeches.

        list of speeches is tuple with parameters:
        - start: float
        - end: float
        - text: str

        Parametrs
        -------
        audio_file_path: str | Path
            Path to the audio file.

        Returns
        -------
        list[Subtitels]
            List of speeches (starts and ends in seconds).
            Text shold be empty string.
        """
        raise NotImplementedError
