from geoforge.core.base import BaseSkill
from geoforge.core.registry import registry

class TestSkill(BaseSkill):
    name = "test"

    def execute(self, **kwargs):
        return {"message": "Hello from GeoForge"}

# IMPORTANT: register skill
registry.register(TestSkill)