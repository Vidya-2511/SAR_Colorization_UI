import numpy as np
import tensorflow as tf
from tensorflow.keras.losses import MeanSquaredError
from PIL import Image

# Load U-Net Model
@st.cache_resource
def load_model():
    model_path = "model/unet_model.h5"  # Make sure the model is in the correct folder
    return tf.keras.models.load_model(model_path, custom_objects={'mse': MeanSquaredError()})

model = load_model()

def load_image(image):
    img = image.convert('L')  # Convert to grayscale
    img = img.resize((128, 128))  # Resize for model
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=(0, -1))  # Shape -> (1, 128, 128, 1)
    return img.astype(np.float32)

def process_image(image):
    input_image = load_image(image)
    prediction = model.predict(input_image)
    predicted_image = (prediction.squeeze() * 255).astype(np.uint8)  # Convert to grayscale
    return Image.fromarray(predicted_image)
