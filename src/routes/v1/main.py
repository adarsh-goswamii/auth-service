from fastapi import APIRouter
from routes.v1 import user, application, oauth

api_router = APIRouter()

api_router.include_router(user.router, prefix='/v1/user', tags=["User"])
api_router.include_router(application.router, prefix='/v1/application', tags=["Application"])
api_router.include_router(oauth.router, prefix='/v1/oauth', tags=["Oauth"])