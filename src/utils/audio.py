import numpy as np

def generate_tone(frequency, duration, sample_rate=44100):
    """
    Generate a sine wave tone for the given frequency and duration.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t)
    return tone
