import unittest
import numpy as np
import os
import soundfile as sf
from src.decoder import decode_audio_to_image

class TestDecoder(unittest.TestCase):
    def test_decode_audio_to_image(self):
        # Create a dummy audio file (1 second of silence)
        dummy_audio = np.zeros(44100, dtype=np.float32)
        dummy_file = "dummy_audio.wav"
        sf.write(dummy_file, dummy_audio, 44100)
        
        try:
            image_array = decode_audio_to_image(dummy_file)
            # Check for expected dummy image shape
            self.assertEqual(image_array.shape, (256, 320))
        finally:
            os.remove(dummy_file)

if __name__ == "__main__":
    unittest.main()
