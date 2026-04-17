from openai import OpenAI
import os


def run_openai(prompt):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return res.choices[0].message.content


def run_mock_claude(prompt):
    return "Claude analysis placeholder"


def run_mock_gemini(prompt):
    return "Gemini analysis placeholder"


def compare_models(prompt):
    return {
        "openai": run_openai(prompt),
        "claude": run_mock_claude(prompt),
        "gemini": run_mock_gemini(prompt)
    }