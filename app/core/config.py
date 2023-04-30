from functools import lru_cache
from decouple import config


class Settings:
    PROJECT_NAME: str = 'dawits-buchi-app33'
    DEBUG: bool = config('FASTAPI_ENV', cast=bool, default=False)
    VERSION: str = '0.1.0'
    ALLOWED_HOSTS: list = config('ALLOWED_HOSTS', default=['*'])
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = config('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MONGO_URI: str = config('DB_URL')
    RABBITMQ_SERVER: str = config('RABBITMQ_SERVER')
    RABBITMQ_USER: str = config('RABBITMQ_USER')
    RABBITMQ_PASSWORD: str = config('RABBITMQ_PASSWORD')
    RABBITMQ_VHOST: str = config('RABBITMQ_VHOST')
    BROKER_URI: str = f'pyamqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_SERVER}//'
    WORKER_QUEUE_NAME: str = 'fastapi-tasks-queue'


@lru_cache()
def get_settings():
    return Settings()
