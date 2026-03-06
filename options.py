import streamlit as st

if st.button("Click me"):
    st.write("Button clicked!")

choice=st.radio("Choose an option: ", ["Billy strings", "Nine inch nails", "TRIVUA"])
st.write("You selected : ", choice)

agree=st.checkbox("I agree")

if agree:
    st.write("Thanks for agreeing!")