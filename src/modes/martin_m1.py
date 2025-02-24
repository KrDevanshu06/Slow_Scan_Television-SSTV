MODE_NAME = "Martin M1"
LINE_DURATION = 0.1  # seconds per line (example)
MIN_FREQUENCY = 1500  # Hz
MAX_FREQUENCY = 2300  # Hz

def pixel_to_frequency_martin(pixel_value):
    """
    Map a pixel value (0-255) to a frequency for Martin M1.
    """
    return MIN_FREQUENCY + (MAX_FREQUENCY - MIN_FREQUENCY) * (pixel_value / 255.0)
