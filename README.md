# AI Book Recommendation System

## Overview
This project is an AI-powered book recommendation system built with Streamlit. It leverages modern NLP models and vector search to provide personalized book suggestions based on user interests.

## Features
- **Conversational AI**: Users can chat with the AI to describe their book preferences.
- **Personalized Recommendations**: The system suggests books tailored to user interests using semantic search.
- **Book Details**: Fetches book covers, descriptions, and links from the Google Books API.
- **Modern UI**: Stylish, interactive interface built with Streamlit and custom CSS.

## Project Structure
```
├── app.py                  # Main Streamlit app entry point
├── requirements.txt        # Python dependencies
├── data/
│   └── books.csv           # Dataset of books
├── ai/
│   └── recommendation_system.py  # AI logic for recommendations
├── ui/
│   ├── components.py       # UI components (book cards, etc.)
│   └── styles.py           # Custom CSS for Streamlit
└── utils/
    ├── book_api.py         # Fetches book info from Google Books API
    └── load_data.py        # Loads and preprocesses book data
```

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Pinecone API key:
     ```
     PINECONE_API_KEY=your_pinecone_api_key
     ```
4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## Requirements
See `requirements.txt` for all dependencies. Key packages:
- streamlit
- pandas
- requests
- python-dotenv
- langchain & related modules
- pinecone
- sentence-transformers

## Data
- The `data/books.csv` file should contain columns: `Title`, `Authors`, `Category`, `Description`.

## Customization
- **AI Model**: Uses `sentence-transformers/all-MiniLM-L6-v2` for embeddings.
- **Vector Store**: Uses Pinecone for semantic search.
- **UI**: Modify `ui/styles.py` and `ui/components.py` for custom look and feel.

## Credits
- Built with [Streamlit](https://streamlit.io/), [LangChain](https://python.langchain.com/), [Pinecone](https://www.pinecone.io/), and [Google Books API](https://developers.google.com/books/docs/v1/using).

---
Feel free to contribute or customize for your own book datasets and recommendation logic!
