import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt

# sidebar

option = st.sidebar.selectbox("Choose function", ["Sine", "Cosine"])

#main content
x = np.linspace(0, 10, 100)
if option == "Sine":
    y = np.sin(x)
else:
    y = np.cos(x)

#plot
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)