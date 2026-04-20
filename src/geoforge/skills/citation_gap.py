from geoforge.core.base import BaseSkill
from geoforge.core.registry import registry

from geoforge.engine.query_simulator import generate_queries
from geoforge.engine.ai_citation import run_model


class CitationGapSkill(BaseSkill):
    name = "geo-engine"

    def execute(self, **kwargs):
        target_url = kwargs.get("target_url")
        competitor_url = kwargs.get("competitor_url")
        topic = kwargs.get("topic", "business")

        queries = generate_queries(topic, n=5)

        results = []
        target_hits = 0
        competitor_hits = 0

        for q in queries:
            res = run_model(q, target_url, competitor_url)

            if res["mentions"]["target_mentioned"]:
                target_hits += 1

            if res["mentions"]["competitor_mentioned"]:
                competitor_hits += 1

            results.append({
                "query": q,
                "result": res
            })

        visibility = int((target_hits / max(1, len(queries))) * 100)

        return {
            "queries": results,
            "summary": {
                "target_mentions": target_hits,
                "competitor_mentions": competitor_hits,
                "visibility_score": visibility
            }
        }


registry.register(CitationGapSkill)