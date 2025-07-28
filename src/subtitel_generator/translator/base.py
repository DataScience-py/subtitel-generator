"""Base translator class."""

from abc import ABC, abstractmethod

from subtitel_generator.subtitel_model import Subtitels


class BaseTranslator(ABC):
    """Base translator class."""

    @abstractmethod
    def generate(self, speeches: list[Subtitels]) -> list[Subtitels]:
        """
        Generate change text in subtitels to needed language.

        Parameters
        ----------
        speeches : list[Subtitels]
            before list of speeches

        Returns
        -------
        list[Subtitels]
            after list of speeches
        """
