"""Comand line for subtitel generator."""

from subtitel_generator import SubtitelGenerator  # main class
from subtitel_generator.file_generator import SrtSubtitleFileGenerator
from subtitel_generator.speech_to_text import VoskSTT  # model for stt
from subtitel_generator.translator import GoogleDeepTranslator
from subtitel_generator.voive_activation_detector import (
    VADSilero,  # model for vad
)

s = SubtitelGenerator(
    vad=VADSilero(),
    stt=VoskSTT(),  # path to vosk model
    file_generater=SrtSubtitleFileGenerator(),
    translator=GoogleDeepTranslator(),
)

while (comand := input("> ")) != "exit":
    s.generate(comand)
