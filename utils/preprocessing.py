from PIL import Image
import numpy as np

def preprocess_image(img):
    if not isinstance(img, Image.Image):
        img = Image.fromarray(img)
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    return img

