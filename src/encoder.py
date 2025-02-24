import numpy as np
from utils.audio import generate_tone
from utils.image import pixel_to_frequency

def encode_line(pixel_values, line_duration=0.1, sample_rate=44100):
    """
    Encode a single line of pixel values into an audio signal.
    """
    line_audio = np.array([])
    pixel_duration = line_duration / len(pixel_values)
    for pixel in pixel_values:
        freq = pixel_to_frequency(pixel)  # Uses default mode (martin_m1)
        tone = generate_tone(freq, pixel_duration, sample_rate)
        line_audio = np.concatenate((line_audio, tone))
    return line_audio

def encode_image_to_audio(image_array, line_duration=0.1, sample_rate=44100):
    """
    Encode an entire image (as a numpy array) into an SSTV audio signal.
    """
    audio_signal = np.array([])
    for row in image_array:
        line_audio = encode_line(row, line_duration, sample_rate)
        audio_signal = np.concatenate((audio_signal, line_audio))
    return audio_signal
