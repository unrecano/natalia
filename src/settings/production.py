import secrets
from settings.base import BaseConfig

class ProductionConfig(BaseConfig):
    SECRET_KEY = secrets.token_urlsafe(32)
    DEBUG = False