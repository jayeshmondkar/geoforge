def extract_domain(url):
    try:
        return url.replace("https://", "").replace("http://", "").split("/")[0]
    except:
        return url


def detect_brand_mentions(answer, target_url, competitor_url):
    text = answer.lower()

    target_domain = extract_domain(target_url).lower()
    competitor_domain = extract_domain(competitor_url).lower()

    return {
        "target_mentioned": target_domain in text,
        "competitor_mentioned": competitor_domain in text
    }