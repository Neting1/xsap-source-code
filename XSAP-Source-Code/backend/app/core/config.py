from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = "Xeonsys Stock Analytics Platform"

    SECRET_KEY: str

    FIREBASE_API_KEY: str

    FIREBASE_CREDENTIALS: str

    SMTP_SERVER: str

    SMTP_PORT: int

    SMTP_EMAIL: str

    SMTP_PASSWORD: str

    SMTP_FROM_NAME: str = "XSAP Alerts"

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()