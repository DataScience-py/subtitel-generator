from deep_translator import GoogleTranslator

from subtitel_generator.subtitel_model import Subtitels

from .base import BaseTranslator


class GoogleDeepTranslator(BaseTranslator):
    """Google Deep Translator class."""

    def __init__(
        self, source_language: str = "auto", target_language: str = "ru"
    ):
        self.model_translator = GoogleTranslator(
            source=source_language, target=target_language
        )

    def generate(self, speeches: list[Subtitels]) -> list[Subtitels]:
        """Translate speches from source language to target language."""
        target_list = self.model_translator.translate_batch(
            speech["text"] for speech in speeches
        )

        for speech, target in zip(speeches, target_list, strict=False):
            speech["text"] = target

        return speeches
