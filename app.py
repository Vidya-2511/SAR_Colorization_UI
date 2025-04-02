'''
import streamlit as st
import time

# Set page config
st.set_page_config(page_title="SAR Image Colorization", page_icon="🎨", layout="wide")

# Apply custom CSS
st.markdown("""
    <style>
        /* Remove Streamlit default padding */
        .block-container { padding: 0 2rem; }
        /* Custom font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
        /* Center main title */
        .main-title { text-align: center; font-size: 3rem; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🎨 Colorization", "📜 About"])

if page == "🏠 Home":
    #st.video("assets/earth_rotation.mp4")  # Background animation
    st.markdown('<h1 class="main-title">Welcome to SAR Image Colorization 🌍</h1>', unsafe_allow_html=True)
    st.write("This project colorizes grayscale SAR images using deep learning.")

elif page == "🎨 Colorization":
    from pages import colorization
    colorization.show()

elif page == "📜 About":
    from pages import about
    about.show()
'''


import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.losses import MeanSquaredError

st.set_page_config(page_title="SAR Image Colorization", layout="wide")

# Load U-Net model
@st.cache_resource
def load_model():
    model_path = "/content/drive/MyDrive/unet_model_2025_01_17.h5"
    return tf.keras.models.load_model(model_path, custom_objects={'mse': MeanSquaredError()})

model = load_model()

def load_image(image):
    img = image.convert('L')
    img = img.resize((128, 128))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=(0, -1))
    return img.astype(np.float32)

def process_image(image):
    input_image = load_image(image)
    prediction = model.predict(input_image)
    predicted_image = (prediction.squeeze() * 255).astype(np.uint8)
    return Image.fromarray(predicted_image)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Colorize", "About"])

# Home Page - Video Background
if page == "Home":
    st.markdown(
        '''
        <style>
        .fullPage {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: -1;
        }
        video {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            object-fit: cover;
            z-index: -1;
        }
        .titleText {
            text-align: center;
            color: white;
            font-size: 40px;
            font-weight: bold;
            margin-top: 20%;
        }
        </style>
        <div class="fullPage">
            <video autoplay loop muted>
                <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
            </video>
        </div>
        <div class="titleText">Welcome to SAR Image Colorization</div>
        ''',
        unsafe_allow_html=True
    )

# Colorize Page - Image Background
elif page == "Colorize":
    st.markdown(
        '''
        <style>
        .colorize-bg {
            background: url('https://source.unsplash.com/1600x900/?satellite,space') no-repeat center center fixed;
            background-size: cover;
            padding: 20px;
            color: white;
            text-align: center;
        }
        </style>
        <div class="colorize-bg">
        <h1>SAR Image Colorization</h1>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.write("Upload a SAR grayscale image and get a predicted optical image.")
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg", "tiff", "tif"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Optical Image"):
            output_image = process_image(image)
            st.image(output_image, caption="Predicted Optical Image", use_column_width=True)

# About Page - Image Background
elif page == "About":
    st.markdown(
        '''
        <style>
        .about-bg {
            background: url('https://source.unsplash.com/1600x900/?technology,ai') no-repeat center center fixed;
            background-size: cover;
            padding: 20px;
            color: white;
            text-align: center;
        }
        </style>
        <div class="about-bg">
        <h1>About This Project</h1>
        <p>This AI model uses U-Net to colorize SAR satellite images.</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
