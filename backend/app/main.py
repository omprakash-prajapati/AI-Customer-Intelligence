from typing import Annotated
from functools import lru_cache
from fastapi import Depends, FastAPI

from .config.settings import Settings
from .api import chat

app = FastAPI()

# Register routers
app.include_router(chat.router)


@lru_cache
def get_settings() -> Settings:
    return Settings()

@app.get("/health")
async def health_check(settings: Annotated[Settings, Depends(get_settings)]):
    return {"status": "ok", "app_name": settings.app_name}

"""
Endpoint
↓
Prompt Builder
↓
Provider Layer
↓
OpenAI
↓
Validation
↓
Response
"""
