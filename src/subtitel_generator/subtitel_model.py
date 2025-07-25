"""Subtitels model."""

from typing import TypedDict


class Subtitels(TypedDict):
    """Result of VAD detection."""

    start: float
    end: float
    text: str
