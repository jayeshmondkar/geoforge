from geoforge.engine.vector_store import embed_text
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_chunks(query, chunks, top_k=3):
    if not chunks:
        return []

    query_emb = embed_text(query)
    chunk_embs = [embed_text(c) for c in chunks]

    scores = cosine_similarity([query_emb], chunk_embs)[0]

    ranked = sorted(zip(chunks, scores), key=lambda x: x[1], reverse=True)

    return ranked[:top_k]