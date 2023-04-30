from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
