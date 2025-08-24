"""Generate subtitel file for .srt."""

import os
from pathlib import Path
from typing import Literal

from subtitel_generator.subtitel_model import Subtitels
from subtitel_generator.utils.logger import get_logger

from .base import BaseSubtitelFileGenerator


class SrtSubtitleFileGenerator(BaseSubtitelFileGenerator):
    """Create subtitel file for .srt."""

    def __init__(self) -> None:
        """Initialize SrtSubtitleFileGenerator."""
        self.logger = get_logger("SRTFileGenerator")

    def generate(
        self,
        audio_file_path: str | Path,
        speeches: list[Subtitels],
    ) -> None:
        """
        Generate create file for .srt file.

        Parameters
        ----------
        file_path : str | Path
            path to audio file
        speeches : list[Subtitels]
            list of times and speeches (text)
        target : bool
            if True, generate from target speeches
        """
        base_path, _ = os.path.splitext(str(audio_file_path))
        subtitel_file_path = base_path + ".srt"
        text: Literal["text"] = "text"

        with open(subtitel_file_path, "w", encoding="utf-8") as file:
            for i, speech in enumerate(speeches):
                print(speech)
                file.write(f"{i + 1}\n")
                file.write(f"{speech['start']} --> {speech['end']}\n")
                file.write(f"{speech[text]}\n")

        self.logger.info(f"File {subtitel_file_path} created.")
