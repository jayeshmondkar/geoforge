from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.create_collection(name="geoforge")


def embed_text(text):
    return model.encode(text).tolist()


def store_chunks(chunks):
    for i, chunk in enumerate(chunks):
        embedding = embed_text(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(i)]
        )


def query_similar(query):
    emb = embed_text(query)
    results = collection.query(query_embeddings=[emb], n_results=3)
    return results