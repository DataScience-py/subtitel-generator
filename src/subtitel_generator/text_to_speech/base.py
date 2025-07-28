"""Base class for stt models."""

from abc import ABC, abstractmethod

from subtitel_generator.subtitel_model import Subtitels


class BaseSTT(ABC):
    """Base class for stt models."""

    @abstractmethod
    def generate(self, speehes: list[Subtitels], audio_file_path: str) -> None:
        """
        Generate create audio file from speeches.

        Parameters
        ----------
        speehes : list[Subtitels]

        """
