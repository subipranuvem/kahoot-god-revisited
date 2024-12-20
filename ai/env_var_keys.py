from enum import StrEnum


class EnvironmentVarKey(StrEnum):
    GEMINI_API_KEY: str = "GEMINI_API_KEY"
    GEMINI_MODEL: str = "GEMINI_MODEL"
