from geoforge.core.base import BaseSkill
from geoforge.core.registry import registry
from bs4 import BeautifulSoup
import requests


class RAGSimulatorSkill(BaseSkill):
    name = "rag-simulate"

    def chunk_text(self, text, size=200):
        words = text.split()
        return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

    def extract(self, url):
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        return " ".join([p.get_text() for p in soup.find_all("p")])

    def score_chunk(self, chunk):
        score = 0
        if len(chunk) > 100:
            score += 1
        if ":" in chunk:
            score += 1
        if any(word in chunk.lower() for word in ["is", "are", "means"]):
            score += 1
        return score

    def execute(self, **kwargs):
        url = kwargs.get("url")

        text = self.extract(url)
        chunks = self.chunk_text(text)

        scored = [{"chunk": c[:200], "score": self.score_chunk(c)} for c in chunks]

        top = sorted(scored, key=lambda x: x["score"], reverse=True)[:5]

        return {"top_chunks": top}


registry.register(RAGSimulatorSkill)