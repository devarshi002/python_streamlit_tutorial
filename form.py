import streamlit as st 
st.markdown("<h1 style = 'text-align: center;'>User Registration</h1>", unsafe_allow_html=True)
with st.form("form 1",clear_on_submit=True):
 col1,col2 = st.columns(2)
 f_name=col1.text_input("first name")
 l_name=col2.text_input("last name")
 st.text_input("Email address")
 st.text_input("password")
 st.text_input("confirm password")
 day,month,year =st.columns(3)
 day.text_input("Day")
 month.text_input("month")
 year.text_input("year")
 s_stat=st.form_submit_button("Submit")

 if s_stat:
  if f_name == "" and l_name == "":
   st.warning("Please fill above fields")
  else:
   st.success("Submitted successfully")