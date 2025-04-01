import streamlit as st

def set_background():
    """Applies background image using custom CSS."""
    background_image = "assets/background.jpg"
    bg_style = f"""
    <style>
    .stApp {{
        background: url({background_image}) no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

def show():
    set_background()  # Set background image

    st.markdown('<h1 style="text-align:center;">📜 About This Project</h1>', unsafe_allow_html=True)

    st.image("assets/background.jpg", use_column_width=True)
    st.write("""
    ## What is SAR Image Colorization?
    - SAR (Synthetic Aperture Radar) is used in remote sensing.
    - Our AI model colorizes SAR images to make them visually interpretable.
    """)

    st.write("""
    ## Team & Contributors
    - **Developer:** [Your Name]
    - **Guide:** [Mentor's Name]
    """)

    st.write("🌍 Made with ❤️ for the competition!")

# Run the function to display the page
show()
