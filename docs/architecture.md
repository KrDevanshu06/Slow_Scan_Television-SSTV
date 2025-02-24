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
│   ├── main.py              # Entry point
│   ├── encoder.py           # Image-to-audio encoding logic
│   ├── decoder.py           # Audio-to-image decoding logic
│   ├── gui.py               # GUI implementation
│   ├── modes/               # SSTV mode-specific implementations
│   │   ├── __init__.py
│   │   ├── martin_m1.py
│   │   └── scottie_s1.py
│   └── utils/               # Utility functions
│       ├── __init__.py
│       ├── audio.py
│       └── image.py
└── tests/
    ├── __init__.py
    ├── test_encoder.py
    └── test_decoder.py

```