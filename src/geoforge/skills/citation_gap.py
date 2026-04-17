from geoforge.core.base import BaseSkill
from geoforge.core.registry import registry
import requests
from bs4 import BeautifulSoup
import os
from openai import OpenAI


class CitationGapSkill(BaseSkill):
    name = "citation-gap"

    def fetch_page(self, url: str) -> str:
        try:
            response = requests.get(url, timeout=10)
            return response.text
        except Exception:
            return ""

    def extract_text(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
        return " ".join(paragraphs[:50])

    def extract_key_reason(self, ai_text: str):
        lines = ai_text.split("\n")
        return lines[:3]

    def ai_analysis(self, target_text: str, competitor_text: str):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
        You are an AI search engine evaluator.

        Compare these two webpages.

        TARGET PAGE:
        {target_text}

        COMPETITOR PAGE:
        {competitor_text}

        Explain:
        1. Which page AI would prefer
        2. Why (specific reasons)
        3. What makes content better for retrieval
        4. Improvements for the weaker page

        Keep answer concise and structured.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content

    def execute(self, **kwargs):
        target_url = kwargs.get("target_url")
        competitor_url = kwargs.get("competitor_url")

        target_html = self.fetch_page(target_url)
        comp_html = self.fetch_page(competitor_url)

        target_text = self.extract_text(target_html)
        comp_text = self.extract_text(comp_html)

        ai_result = self.ai_analysis(target_text, comp_text)

        return {
            "analysis": ai_result,
            "key_reasons": self.extract_key_reason(ai_result)
        }


# Register skill
registry.register(CitationGapSkill)