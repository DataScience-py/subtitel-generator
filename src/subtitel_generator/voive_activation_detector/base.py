"""Base VAD class for all VAD implementations."""

from abc import ABC, abstractmethod
from typing import Any, NamedTuple


class SppechingResult(NamedTuple):
    """Result of VAD detection."""

    start: float
    end: float


class BaseVAD(ABC):
    """Base Voice Activation Detection class (Abstract Base Class)."""

    @abstractmethod
    def vad_detect(self, audio: Any) -> list[SppechingResult]:
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
