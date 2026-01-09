import faiss
from sentence_transformers import SentenceTransformer
from load_docs import load_documents

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = load_documents()
embeddings = model.encode(documents)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def search(query, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    return [documents[i] for i in indices[0]]
