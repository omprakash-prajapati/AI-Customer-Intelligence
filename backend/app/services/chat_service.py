from app.providers.google_provider import GoogleProvider
from app.providers.openai_provider import OpenAIProvider
from app.config.settings import settings


class ChatService:
    def __init__(self, provider: str, api_key: str) -> None:
        self.provider = provider
        self.api_key = api_key
        self.base_url = settings.google_provider_base_url

    def chat(self, model) -> str:
        if self.provider == "openai":
            return OpenAIProvider(model=model, api_key=self.api_key)
        elif self.provider == "google":
            return GoogleProvider(model=model, api_key=self.api_key, base_url=self.base_url)
        else:
            raise ValueError(f"Invalid provider: {self.provider}")
