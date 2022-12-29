from sqlalchemy.orm import Session
from sqlalchemy.sql import or_

from app.models.users import User
from app.schemas.users import UserCreate, UserProfileIn


def get_users(
    db: Session,
    text: str = None,
    min_followers: int = None,
    max_followers: int = None,
):
    query = db.query(User)
    if text:
        text = f"%{text}%"
        query = query.filter(or_(User.username.ilike(text), User.bio.ilike(text)))
    if max_followers:
        query = query.filter(User.followers <= max_followers)
    if min_followers:
        query = query.filter(User.followers >= min_followers)

    return query.order_by(User.created_at.asc()).all()


def get_user(db: Session, email):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_in: UserCreate):
    user = User(email=user_in.email.lower())
    user.make_password(user_in.password.get_secret_value())

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(db: Session, user: User, user_in: UserProfileIn):
    db.query(User).filter(User.id == user.id).update(
        {
            "username": user_in.username,
            "bio": user_in.bio,
            "followers": user_in.followers,
        }
    )

    db.commit()
    db.refresh(user)

    return user
