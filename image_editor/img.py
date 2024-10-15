import streamlit as st
from PIL import Image
st.markdown("Image Editor")
st.markdown("---")
image=st.file_uploader("Upload your Image", type=["jpg","png","jpeg"])
info=st.empty()
size=st.empty()
mode=st.empty()
format_=st.empty()
if image:
    img=Image.open(image)
    info.markdown("<h2 style='text-align: center;'>Information</h2>", unsafe_allow_html=True)
    size=st.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html= True)
    mode=st.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html= True)
    format_=st.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html= True)
    st.markdown("<h2 style='text-align: center;'>Resize</h2>", unsafe_allow_html=True)
    width= st.number_input("width", value=img.width)
    height= st.number_input("height", value=img.height)
    st.markdown("<h2 style='text-align: center;'>Rotation</h2>", unsafe_allow_html=True)
    degree=st.number_input("Degree")
    st.markdown("<h2 style='text-align: center;'>Filter</h2>", unsafe_allow_html=True)
    filters=st.selectbox("filters", options=("None", "Blur", "Detail","Emboss","Smooth"))
    s_btn = st.button("submit")
    if s_btn:
        edited=img.resize((width,height)).rotate(degree)
        st.image(edited)

