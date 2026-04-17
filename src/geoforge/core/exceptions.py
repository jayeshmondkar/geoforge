class GeoForgeError(Exception):
    pass

class SkillNotFoundError(GeoForgeError):
    pass

class SkillRegistrationError(GeoForgeError):
    pass

class SkillExecutionError(GeoForgeError):
    pass

class SkillValidationError(GeoForgeError):
    pass
