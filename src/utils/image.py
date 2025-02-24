from PIL import Image
import numpy as np
from src.modes.martin_m1 import pixel_to_frequency_martin
from src.modes.scottie_s1 import pixel_to_frequency_scottie

def load_image(image_path, width, height):
    """
    Load an image, convert to grayscale, and resize.
    """
    img = Image.open(image_path).convert("L")
    img = img.resize((width, height))
    return np.array(img)

def save_image(image_array, output_path):
    """
    Save a numpy array as an image.
    """
    img = Image.fromarray(image_array)
    img.save(output_path)

def pixel_to_frequency(pixel_value, mode="martin_m1"):
    """
    Map a pixel value to frequency using the selected mode.
    """
    if mode == "martin_m1":
        return pixel_to_frequency_martin(pixel_value)
    elif mode == "scottie_s1":
        return pixel_to_frequency_scottie(pixel_value)
    else:
        # Default to Martin M1 if mode unrecognized
        return pixel_to_frequency_martin(pixel_value)
