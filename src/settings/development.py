from .base import BaseConfig

class DevelopmentConfig(BaseConfig):
    SECRET_KEY = "ANOTHER RANDOM SECRET KEY"
    TESTING = True
    ENV = "development"