import faiss
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def search(query, documents, index, k=5):
    query_embedding = EMBEDDING_MODEL.encode([query])
    distances, indices = index.search(query_embedding, k)

    results = [(documents[i], distances[0][idx]) for idx, i in enumerate(indices[0])]
    return results