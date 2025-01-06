from fastapi import APIRouter
from routes.v1 import user, application

api_router = APIRouter()

api_router.include_router(user.router, prefix='/v1/user', tags=["User"])
api_router.include_router(application.router, prefix='/v1/application', tags=["Application"])