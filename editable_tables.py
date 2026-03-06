import streamlit as st
import pandas as pd

data={
    "name": "alice",
    "age": 25,
    "skills": ["python", "streamlit", "css"]}

df=pd.DataFrame(data)

editable_df=st.data_editor(df, num_rows="dynamic")
st.write("Updated DataFrame")
st.write(editable_df)




