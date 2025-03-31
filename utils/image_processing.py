import numpy as np
from skimage.filters import unsharp_mask

def preprocess_input(image):
    """Normalize and reshape the input image for model."""
    image = image / 255.0
    image = np.expand_dims(image, axis=-1)
    return image.astype(np.float32)

def enhance_output(image):
    """Apply unsharp masking for better details."""
    return (unsharp_mask(image, radius=1, amount=1) * 255).astype(np.uint8)