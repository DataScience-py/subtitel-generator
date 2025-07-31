"""Base class for subtitel module generator."""

from abc import ABC, abstractmethod
from pathlib import Path

from subtitel_generator.subtitel_model import Subtitels


class BaseSubtitelFileGenerator(ABC):
    """Base class for generate subtitel file."""

    @abstractmethod
    def generate(
        self,
        audio_file_path: str | Path,
        speeches: list[Subtitels],
        target: bool,
    ) -> None:
        """
        Generate Create file.

        Parameters
        ----------
        audio_file_path : str | Path
            path to audio file
        speeches : list[Subtitels]
            list of times snd text
        trget : bool
            if True, generate from target speeches
        """
