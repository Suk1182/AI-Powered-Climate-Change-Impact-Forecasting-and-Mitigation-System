
import streamlit as st
from dashboard import create_dashboard

st.title("Climate Impact Forecasting Dashboard")
st.write("Explore the forecasted climate impacts and recommended mitigation strategies.")

if st.button('Show Dashboard'):
    create_dashboard()
