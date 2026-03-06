import streamlit as st

age=st.slider("Select your age : ", 0, 100, 25)
st.write("Age: " , age)


number =st.number_input("Enter a number", min_value=0, max_value=100, value=10)
st.write("Number: " ,number)

name=st.text_input("Enter your name: ")

st.write("Hello: " , name)

bio=st.text_area("Write a short bio: ")
st.write("Your bio: ", bio)