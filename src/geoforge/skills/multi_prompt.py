from geoforge.core.base import BaseSkill
from geoforge.core.registry import registry
from geoforge.skills.citation_gap import CitationGapSkill


class MultiPromptSkill(BaseSkill):
    name = "multi-prompt"

    def generate_prompts(self, topic: str):
        return [
            f"What is {topic}?",
            f"Best {topic} platforms",
            f"Top alternatives to {topic}",
            f"How to choose {topic}",
            f"{topic} vs competitors"
        ]

    def execute(self, **kwargs):
        topic = kwargs.get("topic")

        prompts = self.generate_prompts(topic)

        results = []

        skill = CitationGapSkill()

        for p in prompts:
            result = skill.execute(
                target_url=kwargs.get("target_url"),
                competitor_url=kwargs.get("competitor_url")
            )
            results.append({
                "prompt": p,
                "analysis": result
            })

        return {"results": results}


registry.register(MultiPromptSkill)