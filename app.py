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
from utils.helpers import process_image

st.set_page_config(page_title="SAR Image Colorization", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Colorize", "About"])

# Home Page
if page == "Home":
    st.markdown("# 🌍 SAR Image Colorization App")
    st.write("Upload grayscale SAR images and get colorized predictions!")

# Colorize Page
elif page == "Colorize":
    st.markdown("## Upload Your SAR Image")
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg", "tiff", "tif"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Optical Image"):
            output_image = process_image(image)
            st.image(output_image, caption="Predicted Optical Image", use_column_width=True)

# About Page
elif page == "About":
    st.markdown("## About This Project")
    st.write("This AI model uses U-Net to colorize SAR images.")

