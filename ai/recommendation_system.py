
import streamlit as st

@st.cache_resource
def load_system(books):
    from langchain_core.documents import Document
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_huggingface import HuggingFaceEmbeddings
    import pinecone
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

    # Use Pinecone classic SDK (v2.x)
    pinecone_api_key = st.secrets["PINECONE_API_KEY"]
    pinecone_env = "us-east-1-aws"  # classic environment string for us-east-1 on AWS
    pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)
    index_name = "book-recommendation"

    if index_name not in pinecone.list_indexes():
        pinecone.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine"
        )

    index = pinecone.Index(index_name)
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