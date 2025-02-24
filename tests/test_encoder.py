import unittest
import numpy as np
from src.encoder import encode_image_to_audio

class TestEncoder(unittest.TestCase):
    def test_encode_image_to_audio(self):
        # Create a dummy grayscale image (gradient)
        dummy_image = np.tile(np.linspace(0, 255, 320, dtype=np.uint8), (256, 1))
        audio_signal = encode_image_to_audio(dummy_image, line_duration=0.1)
        # Check that the audio signal is non-empty
        self.assertGreater(len(audio_signal), 0)

if __name__ == "__main__":
    unittest.main()
