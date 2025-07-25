"""
Test vad model.

Test vad model:
- SileroVAD
"""

from subtitel_generator import SubtitelGenerator
from subtitel_generator.speech_to_text import VoskSTT
from subtitel_generator.voive_activation_detector import VADSileroDetector


def test_silero_vad() -> None:
    """Test vad model."""
    generator = SubtitelGenerator(
        vad=VADSileroDetector(),
        stt=VoskSTT(
            "/home/anton/projects/subtitel-generator/models/vosk-model-small-en-us-0.15"
        ),
    )  # TODO: make fixture (change None to module)
    generator.vad_generate(
        "/home/anton/projects/subtitel-generator/example/example_audio_5s.wav"
    )
