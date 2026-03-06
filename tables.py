import streamlit as st
import pandas as pd

data={
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 21, 32],
    "City": ['New york', 'los angeles', 'london']

}

df=pd.DataFrame(data)

st.write('### Using st.write() for dataframe')

st.write(df)

st.write('Static Table')
st.table(df)

st.write("interactive table")
st.table(df)

