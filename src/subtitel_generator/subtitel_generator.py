"""Module for the Bsae class of the application.

Get some modules, when be important for the application.

- VoiceActivationDetection module for generate times, when need subtitels.
- SpeechToText module for generate text from voice. Use output from
VoiceActivationDetection module.
- Translater module for translate text.

Supported languages:
Have support any langiuge. We want you can use any language.
We can use any models for generate subtitel. (your own or our)
"""

from logging import Logger
from pathlib import Path

import magic
from moviepy import VideoFileClip

from .file_generator import BaseSubtitelFileGenerator
from .speech_to_text import BaseSTT
from .subtitel_model import Subtitels, Timestamps
from .translator import BaseTranslator
from .utils import timer
from .utils.logger import get_logger
from .voive_activation_detector import BaseVAD


class SubtitelGenerator:
    """Main application class."""

    def __init__(
        self,
        vad: BaseVAD,
        stt: BaseSTT,
        file_generater: BaseSubtitelFileGenerator,
        translator: BaseTranslator | None = None,
    ) -> None:
        """
        __init__ object of the class.

        Parameters
        ----------
        vad : BaseVAD
            Voioce activation detector class
        stt : BaseSTT
            Speech to text class
        file_generater : BaseSubtitelFileGenerator
            when generate subtitels
        translator : BaseTranslator | None, optional
            translator text, by default None
        """
        self.logger: Logger = get_logger("SubtitelGenerator")
        self.vad: BaseVAD = vad
        self.stt: BaseSTT = stt
        self.translater = translator
        self.file_generater = file_generater

    @timer
    def vad_generate(self, audio_file_path: str | Path) -> list[Timestamps]:
        """
        vad_generate return result from voice activation detector.

        Parameters
        ----------
        audio_file_path : str | Path
            path to audio file, where we need detect times

        Returns
        -------
        list[Timestamps]
            List of times, when need subtitels. label text is empty string.
        """
        return self.vad.detect(audio_file_path=audio_file_path)

    @timer
    def stt_generate(
        self, audio_file_path: str | Path, timesamps_speeches: list[Timestamps]
    ) -> list[Subtitels]:
        """
        stt_generate return result from speech to text.

        Parameters
        ----------
        audio_file_path : str | Path
            path to audio file, where we need generate text

        timesamps_speeches : list[Timestamps]
            List of times, when need subtitels

        Returns
        -------
        list[Subtitels]
            List of times with subtitels
        """
        return self.stt.generate(
            audio_file_path=audio_file_path,
            timestamps_speeches=timesamps_speeches,
        )

    @timer
    def file_generate(
        self,
        audio_file_path: str | Path,
        speeches: list[Subtitels],
    ) -> None:
        """
        file_generate create file with subtitels.

        Parameters
        ----------
        audio_file_path : str | Path
            path to audio file, where we need generate subtitels
        speeches : list[Subtitels]
            list of times with speeches (text)
        trget : bool
            if True, generate from target speeches

        Returns
        -------
        None
            Return nthing. CREATE FILE!
        """
        return self.file_generater.generate(
            audio_file_path=audio_file_path, speeches=speeches
        )

    @timer
    def translate(self, speeches: list[Subtitels]) -> list[Subtitels]:
        """
        Translate text from source to target language.

        Parameters
        ----------
        speeches : list[Subtitels]
            list of times with speeches (text)

        Returns
        -------
        list[Subtitels]
            list of times with speeches (text)
        """
        return (
            self.translater.generate(speeches=speeches)
            if self.translater
            else speeches
        )

    def generate_from_audio(self, audio_file_path: str | Path) -> None:
        """
        Generate create subtitels from audio file.

        Parameters
        ----------
        file_path : str | Path
            path to audio file, where we need generate subtitels
        """
        timesamps_speeches = self.vad_generate(audio_file_path=audio_file_path)
        subtitels = self.stt_generate(
            audio_file_path=audio_file_path,
            timesamps_speeches=timesamps_speeches,
        )

        subtitels = self.translate(speeches=subtitels)

        self.file_generate(
            audio_file_path=audio_file_path,
            speeches=subtitels,
        )

    def generate(self, file_path: str | Path) -> None:
        audio_file_path: str | None = None
        if magic.from_file(file_path, mime=True)[:5] == "video":
            audio_file_path = self.convert_video_to_audio(str(file_path))
        self.generate_from_audio(
            audio_file_path=audio_file_path
            if audio_file_path is not None
            else file_path
        )

    def convert_video_to_audio(
        self,
        src_path: str,
    ) -> str:
        clip = VideoFileClip(src_path)
        out_path = f"{src_path.rsplit('.', 1)[0]}.wav"
        clip.audio.write_audiofile(
            out_path,
            logger=None,
        )
        clip.close()
        return out_path
