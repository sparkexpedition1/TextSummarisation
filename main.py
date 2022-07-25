import streamlit as st
import pydaisi as pyd
import pandas as pd
def printSummary(text):
    st.header(text)

st.set_page_config(layout = "wide")
text = st.sidebar.text_input("Text", "Sample Text")
printSummary(text)
