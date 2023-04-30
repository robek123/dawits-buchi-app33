from typing import Any, Dict, Optional, Union

from pymongo import MongoClient
from bson import ObjectId

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from decouple import config


client: AsyncIOMotorClient


def get_client() -> AsyncIOMotorClient:
    global client
    return client


async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(config('DB_URL'))


async def close_mongo_connection():
    client.close()


async def get_database() -> AsyncIOMotorDatabase:
    db = client[b'dawits-buchi-app33']
    return db
