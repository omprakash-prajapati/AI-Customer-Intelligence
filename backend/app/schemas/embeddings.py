from pydantic import BaseModel


class EmbeddedFeedback(BaseModel):
    id: int
    text: str
    embedding: list[float]
