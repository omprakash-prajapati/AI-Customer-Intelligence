from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "AI Customer Intelligence"

    # Database settings
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    # Open AI key
    openai_api_key: str
    chat_provider: str
    chat_model: str
    feedback_provider: str
    feedback_model: str

    # Google API Creds
    google_api_key: str
    google_project_name: str
    google_project_number: str
    google_provider_base_url: str

    # Configurations
    llm_timeout_seconds: int
    llm_max_retries: int

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

@lru_cache
def get_settings() -> Settings:
    return Settings()
