"""Base speech to text model."""

from abc import ABC, abstractmethod
from pathlib import Path

from subtitel_generator.subtitel_model import Subtitels


class BaseSTT(ABC):
    """Base speech to text model."""

    @abstractmethod
    def stt_generate(
        self, audio_file: str | Path, timestamps_speech: list[Subtitels]
    ) -> list[Subtitels]:
        """ADD text for subtitels."""
