import streamlit as st

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.markdown(html_content, unsafe_allow_html=True)
