import time
from geoforge.skills.citation_gap import CitationGapSkill

def monitor(target, competitor, interval=3600):
    skill = CitationGapSkill()

    while True:
        result = skill.execute(
            target_url=target,
            competitor_url=competitor
        )

        print("Monitoring result:", result)

        time.sleep(interval)