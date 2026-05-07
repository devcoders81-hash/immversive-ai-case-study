import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from embeddings.embedder import EmbeddingModel
from vectorstore.chroma_store import ChromaStore
from llm.groq_generator import GroqGenerator


st.title("Indic Manuscript Conversational RAG")

query = st.text_input(
    "Ask a question"
)

if query:

    embedder = EmbeddingModel()

    vector_store = ChromaStore()

    llm = GroqGenerator()

    query_embedding = embedder.encode([query])[0]

    results = vector_store.search(
        query_embedding,
        top_k=3
    )

    documents = results["documents"][0]

    context = "\n".join(documents)

    answer = llm.generate_answer(
        query,
        context
    )

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Retrieved Context")

    for doc in documents:
        st.write(doc)
        st.write("---")