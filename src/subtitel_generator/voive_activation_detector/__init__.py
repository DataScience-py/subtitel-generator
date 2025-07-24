"""Initialize VAD classes."""

from .base import BaseVAD, SppechingResult
from .vad_silero_model import VADSileroDetector

__all__ = ["BaseVAD", "SppechingResult", "VADSileroDetector"]
