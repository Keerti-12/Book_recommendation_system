import streamlit as st
from dotenv import load_dotenv

from utils.load_data import load_books
from utils.book_api import get_book_data
from ai.recommendation_system import load_system
from ui.styles import load_css
from ui.components import render_book_card

load_dotenv()

st.set_page_config(
    page_title="AI Book Recommender",
    page_icon="📚",
    layout="wide"
)

load_css()

st.markdown('<div class="main-title">📚 AI Book Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover books powered by AI</div>', unsafe_allow_html=True)

books = load_books()
retrieval_chain, vector_store = load_system(books)

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "interest" not in st.session_state:
    st.session_state.interest = None

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

query = st.chat_input("Tell AI what kind of books you like...")

if query:
    st.session_state.interest = query
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("assistant"):
        with st.spinner("Finding recommendations..."):
            response = retrieval_chain.invoke({"input": query})
            answer = response["answer"]
            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

# ---------------- RECOMMENDED BOOKS ----------------
if st.session_state.interest:
    st.markdown('<div class="section-title">⭐ Recommended For You</div>', unsafe_allow_html=True)

    docs = vector_store.similarity_search(
        st.session_state.interest,
        k=6
    )

    cols = st.columns(3)
    i = 0

    for doc in docs:

        # safer title extraction
        title = doc.metadata.get("title")

        if not title:
            lines = doc.page_content.split("\n")
            for line in lines:
                if line.startswith("Title:"):
                    title = line.replace("Title:", "").strip()
                    break

        if not title:
            continue

        cover, desc, link = get_book_data(title)

        if cover is None:
            continue

        with cols[i % 3]:
            render_book_card(
                title,
                cover,
                desc,
                link,
                st.session_state.interest
            )

        i += 1

# ---------------- SIMILAR BOOKS ----------------
st.markdown('<div class="section-title">📖 Similar Books</div>', unsafe_allow_html=True)

cols = st.columns(3)
count = 0

for _, row in books.sample(len(books)).iterrows():
    cover, desc, link = get_book_data(row["Title"])

    if cover is None:
        continue

    with cols[count % 3]:
        render_book_card(
            row["Title"],
            cover,
            desc,
            link
        )

    count += 1
    if count == 6:
        break