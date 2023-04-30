from passlib.context import CryptContext
from decouple import config

crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return crypt_context.hash(password)


SECRET_KEY = config('SECRET_KEY')

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30
