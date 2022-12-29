from fastapi import APIRouter

from .users import routes as user_routes

router = APIRouter(prefix="/api", tags=["apis"])
router.include_router(user_routes)
