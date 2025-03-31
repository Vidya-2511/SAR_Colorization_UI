import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
from utils.image_processing import preprocess_input, enhance_output
from utils.evaluation import calculate_metrics

# Load model
@st.cache_resource
def load_model():
    url = "https://huggingface.co/vidya2511/SAR_Colorization_Model/resolve/a445d3ed853c286f4f441b439cd5c0d5ad75af32/unet_model.h5"
    model_path = tf.keras.utils.get_file("unet_model.h5", url)
    return tf.keras.models.load_model(model_path)

model = load_model()

def show():
    st.markdown('<h1 style="text-align:center;">🎨 SAR Image Colorization</h1>', unsafe_allow_html=True)

    # Upload section
    uploaded_file = st.file_uploader("Upload a SAR Image", type=["png", "jpg", "jpeg", "tif"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("L")
        st.image(image, caption="Original SAR Image", width=300)

        if st.button("Colorize"):
            st.write("⏳ Processing...")
            image_np = np.array(image)
            processed = preprocess_input(image_np)
            prediction = model.predict(processed[np.newaxis, ..., np.newaxis])
            colorized = enhance_output(prediction.squeeze())

            st.image(colorized, caption="Colorized Image", width=300)

            # Evaluation
            psnr, ssim, mse = calculate_metrics(image_np, colorized)
            st.write(f"📊 **Metrics:** PSNR: {psnr:.2f} | SSIM: {ssim:.2f} | MSE: {mse:.2f}")

            st.download_button("📥 Download Colorized Image", data=colorized.tobytes(), file_name="colorized.png", mime="image/png")