"""Base speech to text model."""

from abc import ABC, abstractmethod
from pathlib import Path

from subtitel_generator.subtitel_model import Subtitels, Timestamps


class BaseSTT(ABC):
    """Base speech to text model."""

    @abstractmethod
    def generate(
        self,
        audio_file_path: str | Path,
        timestamps_speeches: list[Timestamps],
    ) -> list[Subtitels]:
        """ADD text for subtitels."""
        raise NotImplementedError("Method not implemented.")
