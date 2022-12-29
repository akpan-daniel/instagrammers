from copy import deepcopy

from jose import JWTError, jwt

from app.config.settings import get_settings

SECRET_KEY = get_settings().secret_key
ALGORITHM = "HS256"


def create_token(data_in: dict):
    data = deepcopy(data_in)
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("email")
    except JWTError:
        return None
