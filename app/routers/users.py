from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import users as user_model
from app.schemas import auth as auth_schema
from app.schemas import users as user_schema
from app.services import users as user_service
from app.utils.auth import create_token

from .dependencies import get_current_user, get_db

routes = APIRouter(
    prefix="/users",
    tags=["users"],
)


@routes.post(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=auth_schema.TokenOut,
)
async def add_user(user_in: user_schema.UserCreate, db: Session = Depends(get_db)):
    try:
        user = user_service.create_user(db, user_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email exists already"
        )

    payload = {"email": user.email}
    token = create_token(payload)

    return {"user": user, "token": token}


@routes.get(
    "/search/",
    status_code=status.HTTP_200_OK,
    response_model=Page[user_schema.UserProfileOut],
)
async def get_users(
    text: str = None,
    min_followers: int = None,
    max_followers: int = None,
    db: Session = Depends(get_db),
):
    """
    Use params size: int and page: int to control pagination
    """
    users = user_service.get_users(db, text, min_followers, max_followers)

    return paginate(users)


@routes.put(
    "/profile/",
    status_code=status.HTTP_200_OK,
    response_model=user_schema.UserProfileOut,
)
async def update_user(
    user_in: user_schema.UserProfileIn,
    db: Session = Depends(get_db),
    user: user_model.User = Depends(get_current_user),
):
    try:
        return user_service.update_user(db, user, user_in)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username exists already",
        )


add_pagination(routes)
