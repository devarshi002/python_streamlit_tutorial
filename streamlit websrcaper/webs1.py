#  


import streamlit as st 
import requests
from bs4 import BeautifulSoup
st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter your keyword")
    search = st.form_submit_button("Search")
    if search:
        page= requests.get("https://unsplash.com/s/photos/{keyword}")
        print(page.status_code)
