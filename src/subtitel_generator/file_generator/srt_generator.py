"""Generate subtitel file for .srt."""

import os
from pathlib import Path

from subtitel_generator.logger import get_logger
from subtitel_generator.subtitel_model import Subtitels

from .base import BaseSubtitelFileGenerator


class SrtSubtitleFileGenerator(BaseSubtitelFileGenerator):
    """Create subtitel file for .srt."""

    def __init__(self) -> None:
        """Initialize SrtSubtitleFileGenerator."""
        self.logger = get_logger("SRTFileGenerator")

    def generate(
        self, audio_file_path: str | Path, speeches: list[Subtitels]
    ) -> None:
        """
        Generate create file for .srt file.

        Parameters
        ----------
        file_path : str | Path
            path to audio file
        speeches : list[Subtitels]
            list of times and speeches (text)
        """
        base_path, _ = os.path.splitext(str(audio_file_path))
        subtitel_file_path = base_path + ".srt"

        with open(subtitel_file_path, "w", encoding="utf-8") as file:
            for i, speech in enumerate(speeches):
                file.write(f"{i + 1}\n")
                file.write(f"{speech['start']} --> {speech['end']}\n")
                file.write(f"{speech['text']}\n\n")

        self.logger.debug(f"File {subtitel_file_path} created.")
