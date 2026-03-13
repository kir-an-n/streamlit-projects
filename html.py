# my streamlit practice 

import streamlit as st

html_code ="""
<div style ='background-color: lightyellow;padding: 10px;>
    <h3>Custom HTML Block</h3>
    <p style='color: green;'>This is green text within a div </p>

</div>




"""

st.markdown(html_code, unsafe_allow_html=True)
