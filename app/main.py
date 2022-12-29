from fastapi import FastAPI

from app.routers import users as user_routes

app = FastAPI(
    title="Instagrammers",
    description="An instagram influencer search portal",
)
app.include_router(user_routes.routes, prefix="/api")
