import streamlit as st

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

content = ""
if uploaded_file is not None:
	content = uploaded_file.read().decode("utf-8")

st.text_area("File Content", content, height=200)