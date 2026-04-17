from geoforge.core.base import BaseSkill
from geoforge.core.registry import registry
from geoforge.engine.vector_store import similarity_score
from geoforge.engine.entity import extract_entities
from geoforge.engine.gap_analyzer import find_semantic_gaps
from geoforge.engine.recommender import generate_recommendations
from geoforge.engine.multi_model import compare_models
from geoforge.engine.db import save_result

import requests
from bs4 import BeautifulSoup
import os
from openai import OpenAI


class CitationGapSkill(BaseSkill):
    name = "citation-gap"

    def fetch_page(self, url: str) -> str:
        try:
            return requests.get(url, timeout=10).text
        except:
            return ""

    def extract_text(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
        return " ".join(paragraphs[:50])

    def extract_key_reason(self, ai_text: str):
        return ai_text.split("\n")[:3]

def ai_analysis(self, target_text: str, competitor_text: str):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
        Compare these pages for AI citation:

        TARGET:
        {target_text}

        COMPETITOR:
        {competitor_text}

        Explain:
        - who wins
        - why
        - improvements
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        return res.choices[0].message.content

    except Exception as e:
        return f"AI analysis unavailable (quota issue). Basic comparison only."

    def execute(self, **kwargs):
        target_url = kwargs.get("target_url")
        competitor_url = kwargs.get("competitor_url")

        target_html = self.fetch_page(target_url)
        comp_html = self.fetch_page(competitor_url)

        target_text = self.extract_text(target_html)
        comp_text = self.extract_text(comp_html)

        ai_result = self.ai_analysis(target_text, comp_text)

        sim = similarity_score(target_text, comp_text)

        target_entities = extract_entities(target_text)
        comp_entities = extract_entities(comp_text)
        missing = list(set(comp_entities) - set(target_entities))

        target_chunks = target_text.split(".")
        comp_chunks = comp_text.split(".")

        semantic_gaps = find_semantic_gaps(target_chunks, comp_chunks)

        recommendations = generate_recommendations(semantic_gaps)

        model_outputs = compare_models(ai_result)

        save_result(ai_result)

        return {
            "analysis": ai_result,
            "key_reasons": self.extract_key_reason(ai_result),
            "similarity_score": round(sim, 3),
            "missing_entities": missing[:10],
            "semantic_gaps": semantic_gaps,
            "recommended_sections": recommendations,
            "model_comparison": model_outputs
        }


registry.register(CitationGapSkill)