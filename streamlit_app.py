import streamlit as st
import math


with st.echo():
    msg = "hello world"
    st.write(msg)
    st.write(math.pi)
    radius = st.number_input("반지름")