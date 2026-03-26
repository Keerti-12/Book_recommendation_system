import streamlit as st

def render_book_card(title, cover, desc, link, interest=None):

    ai_tag = ""
    if interest:
        ai_tag = f'<div class="ai-tag">Recommended because you like: {interest}</div>'

    st.markdown(
        f"""
        <div class="flip-card">
            <div class="flip-inner">
                <div class="flip-front">
                    <img src="{cover}">
                    <div>{title}</div>
                </div>
                <div class="flip-back">
                    <div>{desc}</div>
                    <a class="read-btn" href="{link}" target="_blank">Read More</a>
                </div>
            </div>
        </div>
        {ai_tag}
        """,
        unsafe_allow_html=True
    )