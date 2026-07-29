from pydantic_settings import BaseSettings, SettingsConfigDict

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

    # Google API Creds
    google_api_key: str
    google_project_name: str
    google_project_number: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
