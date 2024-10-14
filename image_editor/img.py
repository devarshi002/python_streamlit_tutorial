import streamlit as st
from PIL import Image
st.markdown("Image Editor")
st.markdown("---")
image=st.file_uploader("Upload your Image", type=["jpg","png","jpeg"])
size=st.empty()
mode=st.empty()
format_=st.empty()
if image:
    img=Image.open(image)
    size.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html= True)
    mode.markdown(f"<h6>Mode: {img.size}</h6>", unsafe_allow_html= True)
    format_.markdown(f"<h6>Format: {img.size}</h6>", unsafe_allow_html= True)
