import streamlit as st

date=st.date_input("Pick a date")
st.write("Selected date: ", date)

time=st.time_input("Pick a time")
st.write("Selected time", time)



