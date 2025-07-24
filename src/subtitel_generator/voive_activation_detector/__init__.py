"""Initialize VAD classes."""

from .base import BaseVAD, SppechingResult
from .VADSilero import VADSileroDetector

__all__ = ["BaseVAD", "SppechingResult", "VADSileroDetector"]
