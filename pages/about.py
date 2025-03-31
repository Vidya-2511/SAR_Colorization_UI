import streamlit as st

def show():
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