import streamlit as st

def set_background_video():
    """Embeds a video as a background in Streamlit using HTML & CSS."""
    background_video = "assets/earth_rotation.mp4"  # Ensure the video is in this location

    video_html = f"""
    <style>
    .stApp {{
        position: relative;
        overflow: hidden;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: rgba(0, 0, 0, 0.5); /* Optional overlay for contrast */
    }}
    video {{
        position: fixed;
        top: 50%;
        left: 50%;
        width: auto;
        height: 100%;
        min-width: 100%;
        min-height: 100%;
        transform: translate(-50%, -50%);
        z-index: -2;
        object-fit: cover;
    }}
    .content {{
        text-align: center;
        color: white;
        background: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 10px;
        width: 60%;
        margin: auto;
    }}
    </style>
    
    <video autoplay loop muted>
        <source src="{background_video}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """
    st.markdown(video_html, unsafe_allow_html=True)

def show():
    set_background_video()  # Apply background video

    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown('<h1>📜 About This Project</h1>', unsafe_allow_html=True)

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

    st.markdown('</div>', unsafe_allow_html=True)

# Run the function to display the page
show()
