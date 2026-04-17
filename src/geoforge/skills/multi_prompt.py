from geoforge.core.base import BaseSkill
from geoforge.core.registry import registry
from geoforge.skills.citation_gap import CitationGapSkill


class MultiPromptSkill(BaseSkill):
    name = "geo-engine"

    def generate_prompts(self, topic: str):
        return [
            f"What is {topic}?",
            f"Best {topic}",
            f"{topic} alternatives",
            f"How to choose {topic}",
            f"{topic} vs competitors",
            f"Top platforms for {topic}",
            f"{topic} pricing",
            f"{topic} features",
            f"Benefits of {topic}",
            f"{topic} examples"
        ]

    def score_result(self, result_text: str):
        score = 0
        if "clear" in result_text.lower():
            score += 2
        if "structured" in result_text.lower():
            score += 2
        if "definition" in result_text.lower():
            score += 2
        if len(result_text) > 200:
            score += 2
        return score

    def execute(self, **kwargs):
        topic = kwargs.get("topic")
        target_url = kwargs.get("target_url")
        competitor_url = kwargs.get("competitor_url")

        prompts = self.generate_prompts(topic)

        skill = CitationGapSkill()

        target_score = 0
        competitor_score = 0
        results = []

        for p in prompts:
            result = skill.execute(
                target_url=target_url,
                competitor_url=competitor_url
            )

            text = str(result)

            score = self.score_result(text)

            competitor_score += score

            results.append({
                "prompt": p,
                "score": score,
                "analysis": result
            })

        total = len(prompts) * 8

        return {
            "summary": {
                "total_prompts": len(prompts),
                "competitor_score": competitor_score,
                "max_score": total,
                "geo_score": round((competitor_score / total) * 100, 2)
            },
            "details": results
        }


registry.register(MultiPromptSkill)