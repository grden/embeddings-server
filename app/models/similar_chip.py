from pydantic import BaseModel, Field, validator
from typing import List, Optional
from app.models.utility import normalize_spaces

class SimilarChipRequest(BaseModel):
    preferred_chip_text: str = Field(..., description="The chip text to match (user's preference)")
    available_chip_texts: List[str] = Field(..., description="Array of all visible chip texts")

    @validator('preferred_chip_text', pre=True)
    def clean_preferred(cls, v: str) -> str:
        return normalize_spaces(v)

    @validator('available_chip_texts', pre=True)
    def clean_available(cls, v: List[str]) -> List[str]:
        return [normalize_spaces(item) for item in v]

class SimilarChipResponse(BaseModel):
    best_match_text: Optional[str] = Field(None, description="The best-matching chip text or null if no match found") 