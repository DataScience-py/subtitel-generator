"""Example for run program."""

from subtitel_generator import SubtitelGenerator
from subtitel_generator.speech_to_text import VoskSTT
from subtitel_generator.voive_activation_detector import VADSileroDetector

s = SubtitelGenerator(
    vad=VADSileroDetector(),
    stt=VoskSTT(
        "/home/anton/projects/subtitel-generator/models/vosk-model-small-en-us-0.15"
    ),  # path to vosk model
)

s.run(
    "/home/anton/projects/subtitel-generator/example/example_audio_5s_vosk.wav"
    # path to audio file
)
