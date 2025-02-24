from PIL import Image
import numpy as np
from modes.martin_m1 import pixel_to_frequency_martin

def load_image(image_path, width, height):
    """
    Load an image, convert it to grayscale, and resize it.
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
    Map a pixel intensity to a frequency based on the selected SSTV mode.
    """
    if mode == "martin_m1":
        return pixel_to_frequency_martin(pixel_value)
    elif mode == "scottie_s1":
        from modes.scottie_s1 import pixel_to_frequency_scottie
        return pixel_to_frequency_scottie(pixel_value)
    else:
        # Default to Martin M1 mapping
        return pixel_to_frequency_martin(pixel_value)
