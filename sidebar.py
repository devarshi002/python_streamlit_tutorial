import streamlit as st 

#sidebar 
st.sidebar.title("Sidebar title")
option = st.sidebar.selectbox("choose an option", ["option 1", "option 2", "option 3"])
st.sidebar.write(f"you selected: {option}")
slider_value = st.sidebar.slider("Select range", 0, 100, 25)
st.sidebar.write(f"Slider_value: {slider_value}")