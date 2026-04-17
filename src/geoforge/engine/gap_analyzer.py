from geoforge.engine.vector_store import embed_text
from sklearn.metrics.pairwise import cosine_similarity


def find_semantic_gaps(target_chunks, comp_chunks, threshold=0.6):
    gaps = []

    target_embeddings = [embed_text(t) for t in target_chunks if t.strip()]
    comp_embeddings = [embed_text(c) for c in comp_chunks if c.strip()]

    for i, comp_emb in enumerate(comp_embeddings):
        similarities = cosine_similarity([comp_emb], target_embeddings)[0]

        if max(similarities) < threshold:
            gaps.append(comp_chunks[i])

    return gaps[:5]