from openai import OpenAI
import os


def generate_recommendations(gaps):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    Based on these missing content areas:

    {gaps}

    Suggest:
    - Section headings
    - What content should be added
    - Format for better AI retrieval
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content