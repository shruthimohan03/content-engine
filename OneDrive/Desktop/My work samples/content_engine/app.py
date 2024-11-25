import streamlit as st
import os
from preprocess import load_and_embed_pdfs, create_faiss_index
from query_engine import search

if "query" not in st.session_state:
    st.session_state["query"] = ""
if "results" not in st.session_state:
    st.session_state["results"] = []

st.title("Content Engine - Query and Compare PDFs")

if "index" not in st.session_state:
    documents, embeddings = load_and_embed_pdfs(os.getenv("PDF_DIRECTORY", "./pdfs"))
    index = create_faiss_index(embeddings)
    st.session_state["documents"] = documents
    st.session_state["index"] = index

# Form
with st.form("query_form", clear_on_submit=False):
    query = st.text_input("Ask a question about the documents:", value=st.session_state["query"], key="input_query")
    submitted = st.form_submit_button("Search")
    clear_clicked = st.form_submit_button("Clear")

    if submitted and query:
        st.session_state["query"] = query
        st.session_state["results"] = search(query, st.session_state["documents"], st.session_state["index"])
    elif submitted and not query:
        st.warning("Please enter a query.")

    if clear_clicked:
        st.session_state["query"] = " "
        st.session_state["results"] = []
        st.rerun()

if st.session_state["results"]:
    st.write("**Results:**")
    for result, score in st.session_state["results"]:
        st.write(f"- **Content:** {result}")
        st.write(f"  **Score:** {score}")
