from fastapi import HTTPException
from fastapi.responses import JSONResponse
from configs.constants import APIResponse, ErrorResponse
from typing import Optional, Any

def success_response(data: Optional[Any] = None, message: str = ""):
    return APIResponse(status="success", message=message, data=data)

def error_response(message: str, data: Optional[Any] = None):
    return ErrorResponse(status="error", message=message, data=data)
