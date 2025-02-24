Below is a comprehensive, in‐depth documentation for your Slow Scan Television (SSTV) software project. This documentation covers everything from project structure and design rationale to installation, usage, testing, and future improvements. You can include this documentation in your project (for example, as `docs/Documentation.md`) and reference it in your README.

---

# Slow Scan Television (SSTV) Software Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Architecture & Design](#architecture--design)
    - [Key Concepts](#key-concepts)
    - [System Components](#system-components)
4. [Project Structure](#project-structure)
5. [Detailed File Descriptions](#detailed-file-descriptions)
    - [Entry Point: `src/main.py`](#entry-point-srcmainpy)
    - [Encoder: `src/encoder.py`](#encoder-srcencoderpy)
    - [Decoder: `src/decoder.py`](#decoder-srcdecoderpy)
    - [Graphical User Interface: `src/gui.py`](#graphical-user-interface-srcguipy)
    - [SSTV Modes: `src/modes/`](#sstv-modes-srcmodes)
    - [Utilities: `src/utils/`](#utilities-srcutils)
    - [Tests: `tests/`](#tests-tests)
6. [Installation & Setup](#installation--setup)
7. [Usage Instructions](#usage-instructions)
    - [Command-Line Interface (CLI)](#command-line-interface-cli)
    - [Graphical User Interface (GUI)](#graphical-user-interface-gui)
8. [Testing](#testing)
9. [Version Control & Code Changes](#version-control--code-changes)
10. [Future Improvements](#future-improvements)
11. [Appendix & References](#appendix--references)

---

## Introduction

Slow Scan Television (SSTV) is a method of transmitting static images over radio frequencies by converting images into audio signals. This software project is designed to provide both encoding (image to audio) and decoding (audio to image) functionalities. In addition, a user-friendly graphical interface (GUI) has been implemented using Tkinter, making the software accessible for end users without requiring command-line expertise.

---

## Project Overview

The SSTV software has been built using Python and leverages several libraries (e.g., Pillow for image processing, NumPy and SciPy for signal processing, and SoundFile for audio handling). The software supports multiple SSTV modes (currently _Martin M1_ and _Scottie S1_), with the possibility to extend to additional modes. 

Key features include:
- **Image Encoding:** Converts a grayscale image into an SSTV audio signal based on selected SSTV mode parameters.
- **Audio Decoding:** Processes an SSTV audio signal to reconstruct an image (currently, this functionality is a placeholder returning a dummy image).
- **Graphical Interface:** Provides an intuitive UI for users to select images or audio files, trigger encoding/decoding, and even play generated audio.
- **Testing:** Includes unit tests to ensure the encoding and decoding functionalities work as expected.

---

## Architecture & Design

### Key Concepts

- **SSTV Mode:** Defines the timing, frequency range, and signal mapping rules. For example, _Martin M1_ and _Scottie S1_ have specific parameters (line duration, minimum/maximum frequencies, etc.).
- **Signal Processing:** The conversion from image pixels to audio tones involves mapping each pixel’s intensity to a specific frequency, then generating sine waves for those frequencies.
- **Modular Design:** The project is broken into logical modules:
  - **Encoder/Decoder:** Core logic for converting between images and audio.
  - **Modes:** SSTV mode definitions and helper functions.
  - **Utilities:** Common functions for audio tone generation and image handling.
  - **GUI:** A separate module to handle user interaction.

### System Components

1. **Command-Line Interface (CLI):** Managed via `src/main.py`, which accepts arguments to either encode or decode.
2. **Graphical User Interface (GUI):** Implemented in `src/gui.py`, offering buttons for file selection, mode selection, and executing encoding/decoding tasks.
3. **Processing Modules:**
   - **Encoder:** Converts images to audio signals.
   - **Decoder:** Converts audio signals back to images.
4. **Mode Definitions:** Located in `src/modes/` – each mode (e.g., Martin M1, Scottie S1) contains parameters and mapping functions.
5. **Utilities:** In `src/utils/`, including functions for audio tone generation and image processing.

---

## Project Structure

```
Slow_Scan_Television-SSTV/
├── README.md
├── requirements.txt
├── setup.py
├── docs/
│   ├── architecture.md      # Architecture overview (this doc) 
│   └── Documentation.md     # Detailed documentation file (this file)
├── src/
│   ├── __init__.py
│   ├── main.py              # CLI entry point
│   ├── encoder.py           # Image-to-audio encoding logic
│   ├── decoder.py           # Audio-to-image decoding logic
│   ├── gui.py               # Graphical User Interface implementation
│   ├── modes/               # SSTV mode definitions and helpers
│   │   ├── __init__.py
│   │   ├── martin_m1.py     # Martin M1 mode parameters and mapping
│   │   └── scottie_s1.py    # Scottie S1 mode parameters and mapping
│   └── utils/               # Utility functions
│       ├── __init__.py
│       ├── audio.py         # Audio signal generation functions
│       └── image.py         # Image processing and conversion functions
└── tests/
    ├── __init__.py
    ├── test_encoder.py      # Unit tests for encoder functionality
    └── test_decoder.py      # Unit tests for decoder functionality
```

---

## Detailed File Descriptions

### Entry Point: `src/main.py`

- **Purpose:** Acts as the central command-line interface. It accepts arguments to either encode an image to an SSTV audio file or decode an SSTV audio file into an image.
- **Key Functions:**
  - Parses command-line arguments using `argparse`.
  - Uses absolute imports from the `src` package (e.g., `from src.encoder import encode_image_to_audio`).
  - Handles calling the encoding/decoding functions and writing output via SoundFile.
- **Usage Examples:**
  - To encode:  
    ```bash
    python src/main.py encode --image path/to/image.png --mode martin_m1 --output output.wav
    ```
  - To decode:  
    ```bash
    python src/main.py decode --audio path/to/audio.wav --output output.png
    ```

### Encoder: `src/encoder.py`

- **Purpose:** Contains functions that transform an image (as a NumPy array) into an audio signal based on the selected SSTV mode.
- **Key Functions:**
  - `encode_line()`: Encodes a single row of pixels into a sequence of audio tones.
  - `encode_image_to_audio()`: Iterates over image rows to build a complete audio signal.
- **Integration:** Uses utilities from `src/utils/audio.py` for tone generation and `src/utils/image.py` for pixel-to-frequency conversion.

### Decoder: `src/decoder.py`

- **Purpose:** Implements the reverse process – converting an audio signal back into an image. (Currently, this is a placeholder that returns a dummy black image.)
- **Key Functions:**
  - `decode_audio_to_image()`: Reads an audio file and produces a dummy image (shape 256×320). Future implementations might include real signal processing to decode actual SSTV transmissions.
- **Integration:** Uses SoundFile to read audio data.

### Graphical User Interface: `src/gui.py`

- **Purpose:** Provides a user-friendly interface to encode images to SSTV audio, decode audio back to images, and play audio files.
- **Key Features:**
  - File selectors for images and audio files.
  - A dropdown for selecting SSTV mode (currently _Martin M1_ and _Scottie S1_).
  - Progress bar feedback and threaded subprocess calls to ensure the UI remains responsive.
  - Uses the command-line interface under the hood by spawning subprocesses that call `src/main.py`.
- **Running the GUI:**  
  ```bash
  python src/gui.py
  ```

### SSTV Modes: `src/modes/`

- **Purpose:** Contains mode-specific parameters and helper functions for converting pixel values to audio frequencies.
- **Files:**
  - **`martin_m1.py`:** Defines constants such as `MIN_FREQUENCY`, `MAX_FREQUENCY`, and a mapping function (`pixel_to_frequency_martin()`).
  - **`scottie_s1.py`:** Similarly, provides parameters and a mapping function for the Scottie S1 mode.
- **Integration:** The utilities in `src/utils/image.py` select the appropriate mode mapping based on user input.

### Utilities: `src/utils/`

- **audio.py**
  - **Purpose:** Provides a function `generate_tone()` that generates a sine wave at a given frequency and duration using NumPy.
- **image.py**
  - **Purpose:** Contains functions for:
    - Loading an image, converting it to grayscale, and resizing it.
    - Saving a NumPy array back to an image.
    - Mapping a pixel value to a frequency using the selected SSTV mode.
- **Integration:** Both the encoder and decoder modules rely on these utility functions.

### Tests: `tests/`

- **Purpose:** Unit tests ensure that both encoding and decoding functionalities work as expected.
- **Files:**
  - **`test_encoder.py`:** Creates a dummy gradient image, encodes it, and verifies that an audio signal is generated.
  - **`test_decoder.py`:** Creates a dummy audio file (1 second of silence) and verifies that decoding returns an image with the expected dimensions.
- **Running Tests:**  
  ```bash
  python -m unittest discover -s tests
  ```

---

## Installation & Setup

### Prerequisites

- **Python 3.x:** Ensure you have Python installed.
- **Virtual Environment (Recommended):** It is best practice to create an isolated Python environment.
- **Required Python Libraries:**  
  The required libraries include Pillow, NumPy, SciPy, SoundFile, and Tkinter (included with standard Python installations).  
  All dependencies are listed in `requirements.txt`.

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/Slow_Scan_Television-SSTV.git
   cd Slow_Scan_Television-SSTV
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   ```
   Activate the environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Version Control:**
   - The project uses Git for version control. Make sure your repository is initialized:
     ```bash
     git init
     git remote add origin https://github.com/YourUsername/Slow_Scan_Television-SSTV.git
     ```

---

## Usage Instructions

### Command-Line Interface (CLI)

The primary entry point for the command-line version is `src/main.py`.

- **Encoding an Image:**
  ```bash
  python src/main.py encode --image path/to/image.png --mode martin_m1 --output output.wav
  ```
  This command:
  - Loads the specified image.
  - Converts it into an SSTV audio file using the selected mode.
  - Writes the resulting audio to `output.wav`.

- **Decoding an Audio File:**
  ```bash
  python src/main.py decode --audio path/to/audio.wav --output output.png
  ```
  This command:
  - Reads the SSTV audio file.
  - Converts it into an image (currently a placeholder image).
  - Saves the image as `output.png`.

### Graphical User Interface (GUI)

The GUI is implemented in `src/gui.py`.

- **Launching the GUI:**
  ```bash
  python src/gui.py
  ```
- **Features Available in the GUI:**
  - **Select Image:** Click the “Select Image” button to browse for an image file.
  - **SSTV Mode Selection:** Choose between “martin_m1” and “scottie_s1” from the dropdown.
  - **Encode Image:** After selecting an image and mode, click “Encode Image” to generate an SSTV audio file (`encoded_sstv.wav`).
  - **Select Audio:** Click the “Select Audio” button to browse for an SSTV audio file.
  - **Decode Audio:** After selecting an audio file, click “Decode Audio” to convert it back to an image (`decoded_image.png`).
  - **Play Audio:** The “Play SSTV Audio” button launches the default audio player to play the generated audio.
  - **Progress Feedback:** A progress bar shows activity during encoding/decoding operations.

---

## Testing

Testing is critical to ensure each functionality works correctly.

- **Running All Tests:**
  From the project root, execute:
  ```bash
  python -m unittest discover -s tests
  ```
- **Test Descriptions:**
  - **`tests/test_encoder.py`:** Validates that encoding a dummy image produces a non-empty audio signal.
  - **`tests/test_decoder.py`:** Checks that decoding a dummy audio file produces an image with the expected dimensions.
- **Continuous Integration:**
  Consider integrating with a CI/CD platform (such as GitHub Actions) to automatically run tests on every commit.

---

## Version Control & Code Changes

### Git Workflow

- **Branching Model:**
  - **`main`:** Contains the stable, production-ready code.
  - **Feature Branches:** Develop new features (e.g., a new SSTV mode) in separate branches and merge them into `main` once tested.
- **Commit Messages:**
  - Use clear, descriptive commit messages. For example:
    ```
    Add GUI improvements and progress indicator to encode/decode operations
    ```
- **Merging & Pull Requests:**
  - Merge code via pull requests to ensure code review and testing before integration.
- **Tagging & Releases:**
  - Use Git tags to mark releases (e.g., `v1.0.0`).

### Code Changes for End Users

- **Customization:**
  - **SSTV Modes:** Users can add new modes by creating additional files in `src/modes/` and updating the `pixel_to_frequency()` function in `src/utils/image.py`.
  - **GUI Customizations:** The GUI can be extended to include additional controls (e.g., real-time audio recording).
- **Configuration:**
  - Future versions might include a configuration file (e.g., YAML or JSON) to set parameters like image dimensions, sample rate, and mode-specific details.

---

## Future Improvements

- **Real SSTV Decoding:**  
  Currently, the decoder returns a dummy image. Future versions could implement proper signal processing (using FFT and demodulation) to reconstruct images accurately from SSTV audio.

- **Additional SSTV Modes:**  
  Expand support to include more SSTV modes such as Robot 36, PD 120, etc.

- **Enhanced GUI:**  
  Incorporate real-time audio recording and display of decoding progress, as well as improved error handling and logging.

- **Performance Optimization:**  
  Optimize the encoding/decoding routines for faster processing, possibly utilizing multi-threading or GPU acceleration for signal processing tasks.

- **User Documentation & Tutorials:**  
  Develop step-by-step guides and video tutorials to help users understand how to use and extend the software.

- **Integration with Radio Hardware:**  
  Future versions might include direct integration with SDR (Software Defined Radio) devices for live transmission and reception of SSTV signals.

---

## Appendix & References

### External Libraries and Tools

- **Pillow:**  
  Used for image processing tasks. [Pillow Documentation](https://pillow.readthedocs.io/)

- **NumPy & SciPy:**  
  Employed for numerical operations and signal processing.  
  [NumPy Documentation](https://numpy.org/doc/)  
  [SciPy Documentation](https://docs.scipy.org/doc/)

- **SoundFile:**  
  Used to read and write WAV audio files. [SoundFile Documentation](https://pysoundfile.readthedocs.io/)

- **Tkinter:**  
  The standard Python GUI toolkit. [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

### References

- **SSTV Standards:**  
  Research on various SSTV modes can be found through amateur radio organizations and the ARRL website.
- **Git & GitHub Best Practices:**  
  [Git Documentation](https://git-scm.com/doc)  
  [GitHub Guides](https://guides.github.com/)

---

## Conclusion

This documentation provides a detailed overview of the SSTV software project, including design, structure, file responsibilities, installation, usage, testing, and future directions. By following these guidelines, contributors and end users can understand the project, run it smoothly, and extend its functionalities as needed.

Feel free to update this documentation as the project evolves. Happy coding and clear transmissions!