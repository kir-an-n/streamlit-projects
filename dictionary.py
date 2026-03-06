import streamlit as  st
import pandas as pd

person={
    "name": "alice",
    "age": 25,
    "skills": ["python", "streamlit", "css"]

}

st.json(person)
st.write("Dictioanry dispalyed with st.write(): ", Person)