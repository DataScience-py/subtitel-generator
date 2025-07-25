"""Init stt modules."""

from .base import BaseSTT
from .vosk_stt_model import VoskSTT

__all__ = ["BaseSTT", "VoskSTT"]
