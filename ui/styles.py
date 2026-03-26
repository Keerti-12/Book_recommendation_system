import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .main-title{
        font-size:58px;
        font-weight:900;
        text-align:center;
        background: linear-gradient(90deg,#6366F1,#22D3EE);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .section-title{
        font-size:30px;
        color:white;
        margin-top:30px;
        font-weight:700;
    }
    </style>
    """, unsafe_allow_html=True)