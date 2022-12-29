import pydantic


class UserCreate(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: pydantic.SecretStr


class UserProfileBase(pydantic.BaseModel):
    followers: int


class UserProfileOut(UserProfileBase):
    username: str | None = None
    bio: str | None = None

    class Config:
        orm_mode = True


class UserProfileIn(UserProfileOut):
    username: str
