"""Initialize VAD classes."""

from .base import BaseVAD
from .vad_silero_model import VADSilero

__all__ = ["BaseVAD", "VADSilero"]
