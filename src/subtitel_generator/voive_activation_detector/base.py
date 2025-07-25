"""Base VAD class for all VAD implementations."""

from abc import ABC, abstractmethod
from pathlib import Path

from subtitel_generator.subtitel_model import Subtitels


class BaseVAD(ABC):
    """Base Voice Activation Detection class (Abstract Base Class)."""

    @abstractmethod
    def vad_detect(self, audio_file: str | Path) -> list[Subtitels]:
        """
        Generate list speeches.

        list of speeches is tuple with parameters:
        - start: float
        - end: float

        Parametrs
        -------
        audio: Any
            Audio data.

        Returns
        -------
        list[SppechingResult]
            List of speeches.
        """
        raise NotImplementedError
