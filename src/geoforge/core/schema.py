from pydantic import BaseModel

class SkillResult(BaseModel):
    success: bool
    data: dict | None = None
    error: str | None = None
