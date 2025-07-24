"""
Test vad model.

Test vad model:
- SileroVAD
"""

from subtitel_generator import SubtitelGenerator
from subtitel_generator.voive_activation_detector import VADSileroDetector


def test_silero_vad() -> None:
    """Test vad model."""
    generator = SubtitelGenerator(vad=VADSileroDetector())
    generator.vad_generate(
        "/home/anton/projects/subtitel-generator/example/example_audio_5s.wav"
    )
