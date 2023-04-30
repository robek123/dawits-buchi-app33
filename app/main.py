from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic.networks import EmailStr
from bson import ObjectId
from decouple import config
from datetime import timedelta, datetime

from app.core.config import get_settings
from app.core.security import get_password_hash, verify_password
from app.api.dependencies import get_token_header
from app.api.models import User, UserCreate, UserUpdate
from app.api.endpoints import router as api_router
from app.core.database import connect_to_mongo, close_mongo_connection


app = FastAPI(
    title=get_settings().PROJECT_NAME,
    version=get_settings().VERSION,
    debug=get_settings().DEBUG,
    root_path=get_settings().API_V1_STR,
    openapi_url=f"{get_settings().API_V1_STR}/openapi.json",
    docs_url=f"{get_settings().API_V1_STR}/docs",
    redoc_url=None
)

app.include_router(
    api_router,
    prefix="/users",
    tags=["users"]
)


@app.on_event("startup")
async def __startup_event():
    await connect_to_mongo()


@app.on_event("shutdown")
async def __shutdown_event():
    await close_mongo_connection()
