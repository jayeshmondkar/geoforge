def detect_citation(chunks, target_url, competitor_url):
    target_hits = 0
    competitor_hits = 0

    for chunk, score in chunks:
        text = chunk.lower()

        if target_url.lower() in text:
            target_hits += 1

        if competitor_url.lower() in text:
            competitor_hits += 1

    return {
        "target_hits": target_hits,
        "competitor_hits": competitor_hits
    }