import streamlit as st 
st.title("uploading files")
st.markdown("---")
image = st.file_uploader("Please upload an image", type=["png","jpg","jpeg"])
if image is not None:
    st.image(image)
###################slider##################3
st.markdown("---")
st.slider("This is slider")
##################text#######################
st.text_input("Enter your course title")

#################text area #####################
st.text_area("Cousre details")

###############date input ################
st.date_input("Enter your registration date")

##############set timer ###################
st.time_input("Specify timer")