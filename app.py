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
