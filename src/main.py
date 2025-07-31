"""Example for run the program."""

from subtitel_generator import SubtitelGenerator  # main class
from subtitel_generator.file_generator import SrtSubtitleFileGenerator
from subtitel_generator.speech_to_text import VoskSTT  # model for stt
from subtitel_generator.translator import GoogleDeepTranslator
from subtitel_generator.voive_activation_detector import (
    VADSilero,  # model for vad
)

# cretate instance of the class with models
s = SubtitelGenerator(
    vad=VADSilero(),
    stt=VoskSTT(),  # path to vosk model
    file_generater=SrtSubtitleFileGenerator(),
    translator=GoogleDeepTranslator(),
)

# generate subtitels from audio file
s.generate(
    audio_file_path="/home/anton/projects/subtitel-generator/example/Example_audio_endlish_small.wav"
    # path to audio file
)
