import os
from langchain.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

PDF_DIRECTORY = os.getenv("PDF_DIRECTORY", "./pdfs")
EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2") 
# The embedding model is pretrained and runs locally by downloading the pre-trained weights
# to the local machine

def load_and_embed_pdfs(pdf_directory):
    documents = []
    embeddings = []

    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_directory, filename))
            pages = loader.load_and_split()
            
            for page in pages:
                documents.append(page.page_content)
                embeddings.append(EMBEDDING_MODEL.encode(page.page_content))
    
    return documents, np.array(embeddings)

def create_faiss_index(embeddings):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index
