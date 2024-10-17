import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

image = st.file_uploader("Upload your Image", type=["jpg", "png", "jpeg"])
if image:
    img = Image.open(image)

    # Display image info
    st.markdown("<h2 style='text-align: center;'>Image Information</h2>", unsafe_allow_html=True)
    st.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html=True)
    st.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    st.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html=True)
    
    # Show original image preview
    st.markdown("<h2 style='text-align: center;'>Original Image Preview</h2>", unsafe_allow_html=True)
    st.image(img, caption="Original Image")

    # Resize section
    st.markdown("<h2 style='text-align: center;'>Resize</h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)

    # Rotation section
    st.markdown("<h2 style='text-align: center;'>Rotation</h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree", value=0)

    # Filter section
    st.markdown("<h2 style='text-align: center;'>Apply Filter</h2>", unsafe_allow_html=True)
    filters = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss", "Smooth"))

    # Submit button
    if st.button("Apply Changes"):
        edited = img.resize((width, height)).rotate(degree)

        # Apply selected filter
        filtered = edited
        if filters == "Blur":
            filtered = edited.filter(BLUR)
        elif filters == "Detail":
            filtered = edited.filter(DETAIL)
        elif filters == "Emboss":
            filtered = edited.filter(EMBOSS)
        elif filters == "Smooth":
            filtered = edited.filter(SMOOTH)

        # Display the edited image
        st.markdown("<h2 style='text-align: center;'>Edited Image Preview</h2>", unsafe_allow_html=True)
        st.image(filtered, caption="Edited Image")

else:
    st.markdown("<h3 style='text-align: center;'>Please upload an image to start editing</h3>", unsafe_allow_html=True)
