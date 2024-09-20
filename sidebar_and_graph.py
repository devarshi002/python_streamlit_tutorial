import streamlit as st 
import pandas as pd
import time as t 
from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0,10,100)
bar_x=np.array([1,2,3,4,5])
opt = st.sidebar.radio("Hello this is side bar", options=("Line", "Bar", "H-Bar"))
if opt == "Line":
 st.header("Line chart")
 st.markdown('---')
 fig = plt.figure()
 plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
 
 plt.plot(x, np.sin(x))
 plt.plot(x, np.cos(x), '--')
 st.write(fig)

elif opt == "Bar":
 st.header("Bar graph")
 st.markdown('---')
 fig=plt.figure()
 plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
 plt.bar(bar_x, bar_x*10)
 st.write(fig)

else:
    st.header("H-Bar")
    st.markdown("---")
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.barh(bar_x*10, bar_x)
    st.write(fig)