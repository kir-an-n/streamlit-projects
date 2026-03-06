from os import name

import streamlit as st

st.header('Hello World')

st.title("Re-execution demo")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}")
else:
    st.write("Please type your name above")

print("Script executed")