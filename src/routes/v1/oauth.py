from fastapi import APIRouter
from starlette.requests import Request

from src.services.oauth.controller import OauthController
from src.services.oauth.serializer import GetAccessTokenInbound, LoginUserInbound

router = APIRouter()

@router.post("/token")
async def get_access_token(request: Request, payload: GetAccessTokenInbound):
    return await OauthController.get_access_token(request, payload)

@router.post ("login")
async def login_user(request: Request, payload: LoginUserInbound):
    return await OauthController.login_user(request, payload)