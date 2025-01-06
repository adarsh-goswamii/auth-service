from fastapi import APIRouter, Request

from services.application.controller import ApplicationController
from services.application.serializer import AddApplicationInbound

router = APIRouter()

@router.post("")
async def add_application(request: Request, payload: AddApplicationInbound):
    return await ApplicationController.add_application(request, payload)