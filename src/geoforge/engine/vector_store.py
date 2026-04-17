import chromadb
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import uuid

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

try:
    collection = client.get_collection(name="geoforge")
except:
    collection = client.create_collection(name="geoforge")


def similarity_score(text1, text2):
    emb1 = model.encode([text1])
    emb2 = model.encode([text2])
    return float(cosine_similarity(emb1, emb2)[0][0])


def embed_text(text):
    return model.encode(text).tolist()


def store_chunks(chunks):
    for chunk in chunks:
        embedding = embed_text(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(uuid.uuid4())]
        )


def query_similar(query):
    emb = embed_text(query)
    return collection.query(query_embeddings=[emb], n_results=3)