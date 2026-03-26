import os
import streamlit as st

@st.cache_resource
def load_system(books):
    from langchain_core.documents import Document
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_huggingface import HuggingFaceEmbeddings
    from pinecone import Pinecone, ServerlessSpec
    from langchain_pinecone import PineconeVectorStore
    from langchain_groq import ChatGroq
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain
    from langchain_classic.chains import create_retrieval_chain

    docs = []

    for _, row in books.iterrows():
        text = f"""
        Title: {row['Title']}
        Author: {row['Authors']}
        Category: {row['Category']}
        Description: {row['Description']}
        """
        docs.append(Document(page_content=text))

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    docs = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    dimension = len(embeddings.embed_query("test"))

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index_name = "book-recommendation"

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)

    stats = index.describe_index_stats()
    if stats.get("total_vector_count", 0) == 0:
        vector_store.add_documents(docs)

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Recommend books based on interests."),
        ("human", "{input}\n\nBooks:\n{context}")
    ])

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector_store.as_retriever(search_kwargs={"k": 6})
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    return retrieval_chain, vector_store