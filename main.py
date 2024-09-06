import streamlit as st 
import pandas as pd
tabel = pd.DataFrame({"Column 1":[1,2,3,4,5,6,7], "Column 2":[11,12,13,14,15,16,17]})
st.title("Hi i am streamlit web application")
st.subheader("Hi i am your subheader")
st.header("Hi i am header")
st.text("Hi i am text function used to write function of paragraph")
st.markdown("**Hello** *world*")
st.markdown("# Hello world") #h1 of html
st.markdown("> Deva") #	> blockquote
st.markdown("""
1. First item
2. Second item
3. Third item
   1. Sub-item one
   2. Sub-item two
4. Fourth item
""") #ordered list

st.markdown("`code`") #Code

st.markdown("---")
st.caption("hi i am caption") #this is caption
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

st.write("## H2")
st.metric(label= "Wind speed", value="120ms⁻¹", delta="1.4ms⁻¹" )
st.metric(label= "Wind speed", value="120ms⁻¹", delta="-1.4ms⁻¹" )
st.table(tabel)
st.dataframe(tabel)