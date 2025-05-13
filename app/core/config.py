from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    auth_token: str
    telegram_api_url: str = "https://api.telegram.org"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
