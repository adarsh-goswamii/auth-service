from fastapi import APIRouter, Request

from services.client.controller import ClientController
from services.client.serializer import CreateClientInbound, UpdateClientInbound

router = APIRouter()

@router.post("")
async def create_client(request: Request, payload: CreateClientInbound):
  return await ClientController.create_client(request, payload=payload)

@router.patch("")
async def update_client(request: Request, payload: UpdateClientInbound):
  return await ClientController.update_client(request, payload)

@router.get("/login")
async def login_client(request: Request, payload):
  return None

@router.delete("")
async def delete_client(request: Request, payload):
  return None
