from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from datetime import datetime
import sqlite3

from geoforge.skills.citation_gap import CitationGapSkill

app = FastAPI()

API_KEYS = {"test-key-123": "user"}
USAGE = {}

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401)

    count = USAGE.get(x_api_key, 0)
    if count >= 5:
        raise HTTPException(status_code=429, detail="Limit reached")

    USAGE[x_api_key] = count + 1
    return API_KEYS[x_api_key]


class Req(BaseModel):
    target_url: str
    competitor_url: str
    topic: str = "business"


def save(data):
    conn = sqlite3.connect("geoforge.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        score INTEGER
    )
    """)

    c.execute(
        "INSERT INTO history (timestamp, score) VALUES (?, ?)",
        (datetime.now().isoformat(), data["summary"]["visibility_score"])
    )

    conn.commit()
    conn.close()


@app.post("/analyze")
def analyze(req: Req, user=verify_api_key):
    skill = CitationGapSkill()

    output = skill.execute(
        target_url=req.target_url,
        competitor_url=req.competitor_url,
        topic=req.topic
    )

    save(output)

    return {"success": True, "data": output}