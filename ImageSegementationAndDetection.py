"""
About:
    Single Image Segmentation for "csv", "py", "png", "jpg" file types 
    to increase file upload size use : streamlit run ImageSegementationAndDetection.py --server.maxUploadSize=1028

Usage:
    Replace contents of segment function 
    Run using :streamlit run ImageSegementationAndDetection.py .
"""

import streamlit as st
import Image
import numpy as np

FILE_TYPES = ["csv", "py", "png", "jpg"]
STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

def segment(uploaded_file):
    return np.zeros((100,100))



def main():
    """Run this function to display the Streamlit app"""
    st.info(__doc__)
    st.title("Upload + Classification Example")
    st.markdown(STYLE, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload file", type=FILE_TYPES)
    show_file = st.empty()
    if not uploaded_file:
        show_file.info("Please upload a file of type: " + ", ".join(FILE_TYPES))
        return
    
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Proessing...")
    res_image = segment(uploaded_file)
    st.image(res_image, caption='Segmented Image')
    
    uploaded_file.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('Stopped due to KeyboardInterrupt')