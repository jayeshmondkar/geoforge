from abc import ABC, abstractmethod
from geoforge.core.schema import SkillResult

class BaseSkill(ABC):
    name: str

    @abstractmethod
    def execute(self, **kwargs):
        pass

    def run(self, **kwargs):
        try:
            result = self.execute(**kwargs)
            return SkillResult(success=True, data=result)
        except Exception as e:
            return SkillResult(success=False, error=str(e))
