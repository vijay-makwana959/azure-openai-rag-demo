import streamlit as st
import requests

st.set_page_config(page_title="Azure OpenAI RAG Demo", layout="centered")

st.title("🤖 Azure OpenAI RAG Chatbot")

question = st.text_input("Ask a question")

if st.button("Ask"):
    if question:
        response = requests.post(
            "http://localhost:8000/ask",
            params={"q": question}
        )
        st.success(response.json()["answer"])
    else:
        st.warning("Please enter a question")
