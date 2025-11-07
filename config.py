from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str = Field()

    web_server_host: str = Field("127.0.0.1")
    web_server_port: int = Field(8000)
    
    webhook_path: str = Field("/webhook")
    webhook_secret: str = Field("webhook-secret")
    webhook_base_url: str
    
    database_url: str = Field("sqlite://db.sqlite3")
    
    model_config = SettingsConfigDict(env_prefix='ELWNC_T_', env_file='.env')


settings = Settings()
