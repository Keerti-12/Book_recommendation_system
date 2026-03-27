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

    .flip-card {
        background-color: transparent;
        width: 250px;
        height: 370px;
        perspective: 1000px;
        margin: 20px auto 20px auto;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .flip-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        border-radius: 18px;
    }
    .flip-card:hover .flip-inner {
        transform: rotateY(180deg);
    }
    .flip-front, .flip-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 18px;
        overflow: hidden;
        background: #18181b;
        color: #fff;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 18px 10px 10px 10px;
    }
    .flip-front img {
        width: 120px;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    .flip-front div {
        font-size: 20px;
        font-weight: 700;
        margin-top: 10px;
        color: #22D3EE;
    }
    .flip-back {
        transform: rotateY(180deg);
        background: #23272f;
        color: #fff;
        font-size: 16px;
        justify-content: flex-start;
        padding-top: 30px;
    }
    .flip-back .read-btn {
        display: inline-block;
        margin-top: 18px;
        padding: 8px 18px;
        background: linear-gradient(90deg,#6366F1,#22D3EE);
        color: #fff;
        border: none;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 16px;
        transition: background 0.3s;
    }
    .flip-back .read-btn:hover {
        background: linear-gradient(90deg,#22D3EE,#6366F1);
    }
    .ai-tag {
        margin-top: 10px;
        font-size: 14px;
        color: #facc15;
        background: #23272f;
        border-radius: 6px;
        padding: 4px 10px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)