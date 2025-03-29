from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "a31243b12hj3gnbamdklaskdas89u9hjdnsandao080uhfsda"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = "sqlite:///./consulta_cep.sqlite3"

settings = Settings()
