"""Initialize VAD classes."""

from .base import BaseVAD
from .vad_silero_model import VADSileroDetector

__all__ = ["BaseVAD", "VADSileroDetector"]
