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
        return " ".join(paragraphs[:50])  # limit content

    def ai_analysis(self, target_text: str, competitor_text: str):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
        Compare these two webpages for AI citation quality.

        TARGET PAGE:
        {target_text}

        COMPETITOR PAGE:
        {competitor_text}

        Answer:
        1. Why competitor might be preferred by AI systems
        2. Key content differences
        3. Specific improvements for target page
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
            "ai_analysis": ai_result
        }


# Register skill
registry.register(CitationGapSkill)