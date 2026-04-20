import os
from openai import OpenAI
from geoforge.engine.brand import detect_brand_mentions

def ask_openai(query):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": query}],
        )

        return res.choices[0].message.content
    except Exception as e:
        return f"ERROR: {str(e)}"


def run_model(query, target_url, competitor_url):
    answer = ask_openai(query)

    mentions = detect_brand_mentions(answer, target_url, competitor_url)

    return {
        "answer": answer[:500],
        "mentions": mentions
    }