from pydantic import BaseModel, validator
import re


class PlotQuestionnaireSchema(BaseModel):
    version_nr: str

    @validator("version_nr")
    def validate_semantic_version(cls, v: str) -> str:
        # TODO: use python semantic versioning library
        semantic_version_pattern = (
            r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
            + r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
            + r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
            + r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
        )

        if not re.match(semantic_version_pattern, v):
            raise ValueError(
                "Version number must follow semantic versioning format (X.Y.Z)"
            )

        return v

    class Config:
        extra = "forbid"  # Reject any unknown fields
