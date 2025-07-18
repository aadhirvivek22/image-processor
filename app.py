import streamlit as st
from algorithm.compressor import Compressor
from PIL import Image
import os
import uuid

st.title("Image Compressor")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
quality = st.slider("Max Quality", 1, 100, 85)

option = st.selectbox(
    "Select Output Format",
    ("JPEG", "PNG", "WEBP"),
)

#Check if user has uploaded a file
if uploaded_file:
    img = Image.open(uploaded_file)
    path = uploaded_file.name

    #retrieve file details in case option button is faulty
    file_detaiils = path.split('.')
    if not option:
        output_format = file_detaiils[-1].upper() if (file_detaiils[-1] and file_detaiils[-1].upper()!="JPG") else "JPEG"
    else:
        output_format = option.upper()

    st.image(img, caption="Original Image", use_column_width=True)

    if st.button("Compress"):
        uid = str(uuid.uuid4()) #unique id for the image file
        input_path = f"temp_input_{uid}.jpg"
        output_path = f"temp_output_{uid}.jpg"

        img.save(input_path)

        compressor = Compressor()
        compressor.compress(input_path=input_path, output_path=output_path, output_format=output_format ,quality=quality)

        st.image(output_path, caption="Compressed Image", use_column_width=True)

        with open(output_path, "rb") as f:
            st.download_button("Download Compressed Image", f, file_name="compressed.jpg")

        #remove the temporary fies from memory once done
        os.remove(input_path)
        os.remove(output_path)
