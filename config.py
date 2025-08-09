from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Aquiles Taxi API"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "aquiles"
    POSTGRES_PASSWORD: str = "aquiles"
    POSTGRES_DB: str = "aquiles"

    REDIS_URL: str = "redis://localhost:6379/0"
    OSRM_URL: str = "http://localhost:5000"

    class Config:
        env_file = ".env"

settings = Settings()
