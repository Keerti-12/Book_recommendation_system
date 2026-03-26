import pandas as pd
import streamlit as st

@st.cache_data
def load_books():
    df = pd.read_csv("data/books.csv")
    df.columns = df.columns.str.strip()
    return df.dropna()