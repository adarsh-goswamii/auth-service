from fastapi import APIRouter
from starlette.requests import Request

from services.oauth.controller import OauthController
from services.oauth.serializer import GetAccessTokenInbound

router = APIRouter()

@router.post("/token")
async def get_access_token(request: Request, payload: GetAccessTokenInbound):
    return await OauthController.get_access_token(request, payload)

