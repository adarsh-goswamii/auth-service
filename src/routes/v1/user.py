from fastapi import APIRouter, Request

from src.services.user.controller import UserController
from src.services.user.serializer import CreateUserInbound, UpdateUserInbound, DeleteUserInbound

router = APIRouter()

@router.post("")
async def create_user(request: Request, payload: CreateUserInbound):
  return await UserController.create_user(request, payload=payload)

@router.patch("")
async def update_user(request: Request, payload: UpdateUserInbound):
    return await UserController.update_user(request, payload)

@router.delete("")
async def delete_user(request: Request, payload: DeleteUserInbound):
    return await UserController.delete_user(request, payload)