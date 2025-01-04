from pydantic import BaseModel
from typing import Any, Optional

class APIResponse(BaseModel):
    status: str = "success"
    message: str
    data: Optional[Any] = None

class ErrorResponse(APIResponse):
    status: str = "error"
    data: Optional[Any] = None

class Regex:
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
