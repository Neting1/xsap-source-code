from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = (
        "Xeonsys Stock Analytics Platform"
    )

    VERSION: str = "1.0.0"

    SECRET_KEY: str
    
    ALGORITHM: str = "HS256"

    FIREBASE_API_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    FIREBASE_CREDENTIALS: str

    SMTP_SERVER: str

    SMTP_PORT: int

    SMTP_EMAIL: str

    SMTP_PASSWORD: str

    SMTP_FROM_NAME: str = (
        "XSAP Alerts"
    )

    class Config:

        env_file = ".env"


settings = Settings()