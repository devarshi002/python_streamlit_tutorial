import streamlit as st
import time as ts
from datetime import time

st.title("Progress Bar Timer with Custom Color")
st.markdown("---")

# Custom CSS to style the progress bar
st.markdown(
    """
    <style>
    .stProgress > div > div > div > div {
        background-color: #FF4B4B;  /* Change this color to your desired one */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to convert time into seconds
def converter(value):
    m, s, ms = value.split(":")
    t_s = int(m) * 60 + int(s) + int(ms) / 1000
    return t_s

# Timer input
val = st.time_input("Set Timer", value=time(0, 0, 0))

if str(val) == "00:00:00":
    st.write("Please set the timer")
else:
    # Convert time input to seconds
    val_seconds = val.hour * 3600 + val.minute * 60 + val.second
    if val_seconds == 0:
        st.write("Please set a non-zero timer")
    else:
        bar = st.progress(0)
        per = val_seconds / 100
        
        # Placeholder for percentage text
        percent_text = st.empty()

        # Progress loop
        for i in range(100):
            bar.progress(i + 1)
            percentage = i + 1
            percent_text.text(f"Progress: {percentage}%")
            ts.sleep(per)
