from typing import Annotated, Optional

from pydantic import BaseModel, Field, EmailStr, root_validator, model_validator

from configs.constants import Regex
from utils.validation import validate_password


class CreateUserInbound(BaseModel):
    name: Annotated[str, Field(max_length=255, min_length=2)]
    email: EmailStr
    password: str

    @model_validator(mode="after")
    def validate_password(self):
        password = self.password
        if password:
            validate_password(password)
        return self

class CreateUserOutbound(BaseModel):
    id: int
    name: str
    email: str

class UpdateUserInbound(BaseModel):
    name: Optional[Annotated[str, Field(max_length=255, min_length=2)]] = None
    password: Optional[str] = None

    @model_validator(mode="after")
    def validate_password(self):
        password = self.password
        if password:
            validate_password(password)
        return self

class DeleteUserInbound(BaseModel):
    email: EmailStr