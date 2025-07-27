"""
Test vad model.

Test vad model:
- SileroVAD
"""

import pytest

from subtitel_generator import SubtitelGenerator
from subtitel_generator.file_generator import SrtSubtitleFileGenerator
from subtitel_generator.speech_to_text import VoskSTT
from subtitel_generator.voive_activation_detector import VADSilero


@pytest.fixture
def en_generator() -> SubtitelGenerator:
    """Model for en sub."""
    return SubtitelGenerator(
        vad=VADSilero(),
        stt=VoskSTT(
            "/home/anton/projects/subtitel-generator/models/vosk-model-small-en-us-0.15"
        ),
        file_generater=SrtSubtitleFileGenerator(),
    )


def test_silero_vad(en_generator: SubtitelGenerator) -> None:
    """Test vad model."""
    en_generator.vad_generate(
        "/home/anton/projects/subtitel-generator/example/Example_audio_endlish_small.wav"
    )
