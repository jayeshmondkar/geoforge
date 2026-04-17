from geoforge.core.base import BaseSkill

class SkillRegistry:
    def __init__(self):
        self.skills = {}

    def register(self, skill_cls):
        self.skills[skill_cls.name] = skill_cls

    def get(self, name):
        return self.skills[name]

    def list(self):
        return list(self.skills.keys())

registry = SkillRegistry()
