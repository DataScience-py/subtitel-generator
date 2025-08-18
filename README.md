# Subtitle Generator

A Python project for generating subtitles from audio files using Voice Activity Detection (VAD) and Speech-to-Text (STT) models.

> The subtitle language matches the language of the selected Vosk model. Subtitles can be generated for any language supported by both Vosk and Silero-VAD models.
> Currently, there is no translation module, so speech is transcribed to text in the original language only.


---

## Features Checklist

- [x] ~~Voice Activity Detection (VAD) using Silero VAD~~
- [x] ~~Speech-to-Text (STT) using Vosk (English )~~
- [x] ~~Support any vosk model.~~
- [x] ~~Subtitle file generation (SRT format)~~
- [ ] Translation support for other languages
- [ ] Text-to-Speech (TTS) integration
- [ ] CLI interface
- [ ] GUI interface
- [ ] Docker support

---

## Current Limitations

- **The subtitle language is determined by the Vosk model you use.**  
  Subtitles can be generated for any language supported by both Vosk and Silero-VAD.
- **No translation module is implemented yet.**  
  Speech is transcribed to text in the original language only.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DataSciense-py/subtitel-generator.git
   cd subtitel-generator
   ```
2. Install dependencies using [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```
3. Download the required Vosk model and place its folder inside the `models/vosk/` directory. For example, for English, use `models/vosk/vosk-en` (where `vosk-en` is any Vosk model folder you want to use).
   No additional setup is required: the program will automatically use the model from the specified folder.

---

## Usage Example

See `src/main.py` for a runnable example. Basic usage:

```python
from subtitel_generator import SubtitelGenerator
from subtitel_generator.file_generator import SrtSubtitleFileGenerator
from subtitel_generator.speech_to_text import VoskSTT
from subtitel_generator.voive_activation_detector import VADSilero

s = SubtitelGenerator(
    vad=VADSilero(),
    stt=VoskSTT(),
    file_generater=SrtSubtitleFileGenerator(),
)

s.generate(audio_file_path="example/Example_audio_endlish_small.wav") # Path to the audio file
```

---

## Project Structure

- `src/subtitel_generator/` — Main package
  - `subtitel_generator.py` — Main orchestration class
  - `file_generator/` — Subtitle file generators (e.g., SRT)
  - `speech_to_text/` — Speech-to-text models (Vosk)
  - `voive_activation_detector/` — Voice activity detection (Silero)
  - `logger/` — Logging utilities
- `models/` — Pretrained models (e.g., Vosk)
- `example/` — Example audio files
- `tests/` — Unit tests

---

## Testing

Run tests with:
```bash
poetry run pytest
```

---

## License

This project is licensed under the terms of the [APACHE2.0 License](LICENSE).

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests.
