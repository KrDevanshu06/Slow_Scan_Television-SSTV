# Martin M1 mode definitions

MODE_NAME = "Martin M1"
LINE_DURATION = 0.1  # seconds per line (example value)
MIN_FREQUENCY = 1500  # Hz
MAX_FREQUENCY = 2300  # Hz

def pixel_to_frequency_martin(pixel_value):
    """
    Map a pixel intensity (0-255) to a frequency for Martin M1 mode.
    """
    return MIN_FREQUENCY + (MAX_FREQUENCY - MIN_FREQUENCY) * (pixel_value / 255.0)
