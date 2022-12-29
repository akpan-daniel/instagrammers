import pydantic

from .users import UserProfileOut


class TokenOut(pydantic.BaseModel):
    token: str
    user: UserProfileOut
