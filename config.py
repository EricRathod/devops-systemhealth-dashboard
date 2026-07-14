import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    """Application configuration."""

    APP_NAME = os.getenv(
        "APP_NAME",
        "DevOps System Health Dashboard",
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0",
    )

    APP_ENV = os.getenv(
        "APP_ENV",
        "development",
    )

    DEBUG = APP_ENV == "development"