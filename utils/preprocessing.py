from PIL import Image
import numpy as np

def preprocess_image(img):
    """
    Resize the input PIL image to 224x224 and normalize pixel values to [0,1].
    """
    img = img.resize((224, 224))
    img = np.array(img).astype(np.float32) / 255.0
    return img
