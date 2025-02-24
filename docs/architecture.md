# Project Architecture

## Overview
The project consists of two main components:
- **Encoder:** Converts an image into an SSTV audio signal.
- **Decoder:** Converts an SSTV audio signal back into an image.

## Directory Structure
```
sstv_projectSlow_Scan_Television-SSTV/
├── README.md
├── requirements.txt
├── setup.py
├── docs/
│   └── architecture.md
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point for running the encoder/decoder
│   ├── encoder.py           # Core image-to-audio encoding logic
│   ├── decoder.py           # Core audio-to-image decoding logic
│   ├── modes/               # SSTV mode-specific implementations
│   │   ├── __init__.py
│   │   ├── martin_m1.py
│   │   └── scottie_s1.py
│   └── utils/               # Utility functions for audio and image processing
│       ├── __init__.py
│       ├── audio.py
│       └── image.py
└── tests/
    ├── __init__.py
    ├── test_encoder.py
    └── test_decoder.py
```