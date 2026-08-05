from pydantic import BaseModel

class SemanticSearchResult(BaseModel):
    id: int
    text: str
    similarity: float
