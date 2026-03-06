import streamlit as st

genre =st.selectbox("Pick a genre: ",["mettal", "rock", "iron", "steel", "wood"])

st.write("Your favourite genre si : ", genre)

metal_subgenre=st.multiselect("Pick your favourite metal genres: ",["thrash metal", "death metal", "black metal"])

st.write("Your favourite metal genre is : ", metal_subgenre)

