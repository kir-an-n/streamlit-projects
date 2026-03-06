import streamlit as st

with st.container():
    st.write("This is inside a container")

col1, col2=st.columns(2)

with col1:
    st.write("Column 1 Content")

with col1: 
    st.write("Column 2 Content")

with st.expander("More info"):
    st.write("Hidden content reveales when the expander is clicked")


option=st.sidebar.selectbox("Select page: ", ["home", "settings", "about"])
st.sidebar.write("Sidebar Content here")

st.write(f"Current page: {option}")

