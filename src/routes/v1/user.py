from fastapi import APIRouter, Request

from services.user.controller import UserController
from services.user.serializer import CreateUserInbound, UpdateUserInbound, LoginUserInbound, DeleteUserInbound

router = APIRouter()

@router.post("")
async def create_user(request: Request, payload: CreateUserInbound):
  return await UserController.create_user(request, payload=payload)

@router.patch("")
async def update_user(request: Request, payload: UpdateUserInbound):
    return await UserController.update_user(request, payload)

@router.post(
    "/login")
async def login_user(request: Request, payload: LoginUserInbound):
    return await UserController.validate_user(request, payload)

@router.delete("")
async def delete_user(request: Request, payload: DeleteUserInbound):
    return await UserController.delete_user(request, payload)