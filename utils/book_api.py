import requests
import streamlit as st

@st.cache_data
def get_book_data(title):
    try:
        url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}"
        res = requests.get(url).json()

        if "items" in res:
            info = res["items"][0]["volumeInfo"]

            cover = info.get("imageLinks", {}).get("thumbnail")
            desc = info.get("description", "No description available")
            link = info.get("infoLink")

            if cover:
                return cover, desc[:200] + "...", link
    except:
        pass

    return None, None, None