from fastapi import Header, HTTPException
from jose import JWTError, jwt
from decouple import config

from app.core.config import Settings


settings = get_settings()


async def get_token_header(x_token: str = Header(...)):
    """Obtains and verifies token in header."""
    try:
        payload = jwt.decode(x_token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        token_scopes = payload.get("scopes", [])
        token_data = payload.get("sub")
        if token_data is None:
            raise HTTPException(status_code=400, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")

    return token_data, token_scopes
