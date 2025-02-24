# SSTV Project

This project implements Slow Scan Television (SSTV) functionality, including encoding images into audio signals and decoding audio signals back into images. It supports multiple SSTV modes such as Martin M1 and Scottie S1.

## Features
- **Image-to-Audio Encoding (Transmission):** Converts images to SSTV audio signals.
- **Audio-to-Image Decoding (Reception):** Converts SSTV audio signals back into images.
- **Mode Support:** Martin M1 and Scottie S1 (expandable).

## Requirements
- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)
- [numpy](https://pypi.org/project/numpy/)
- [scipy](https://pypi.org/project/scipy/)
- [soundfile](https://pypi.org/project/SoundFile/)

## Installation

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
