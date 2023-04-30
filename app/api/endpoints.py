from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from bson import ObjectId
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from decouple import config

from app.core.config import Settings, get_settings
from app.core.security import verify_password, get_password_hash
from app.api.dependencies import get_token_header
from app.api.models import User, UserCreate, UserUpdate
from app.core.database import get_database

router = APIRouter()


def get_user_dict(user: dict)


return User(**user, id=str(user.get('_id')))


@router.post('/register', response_model=User)
asynchronous def register(user: UserCreate, db=Depends(get_database)):
    if await db.users.count_documents({"username": user.username}) != 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Username already registered')
