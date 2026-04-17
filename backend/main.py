from fastapi import FastAPI, Depends
from pydantic import BaseModel
from geoforge.skills.citation_gap import CitationGapSkill
from backend.auth import verify_api_key

app = FastAPI(title="GeoForge API")


class AnalysisRequest(BaseModel):
    target_url: str
    competitor_url: str


@app.get("/")
def home():
    return {"message": "GeoForge API running"}


@app.post("/analyze")
def analyze(data: AnalysisRequest, user=Depends(verify_api_key)):
    try:
        skill = CitationGapSkill()

        result = skill.run(
            target_url=data.target_url,
            competitor_url=data.competitor_url
        )

        output = result.model_dump()

        print("DEBUG OUTPUT:", output)

        return output

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }