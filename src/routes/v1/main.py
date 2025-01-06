from fastapi import APIRouter
from routes.v1 import user, client

api_router = APIRouter()

api_router.include_router(user.router, prefix='/v1/user', tags=["User"])
api_router.include_router(client.router, prefix='/v1/client', tags=["Client"])