from typing import Annotated, Optional

from pydantic import BaseModel, Field, EmailStr, model_validator, field_validator

from configs.constants import Regex
from utils.validation import validate_password, validate_domain


class CreateClientInbound(BaseModel):
    name: Annotated[str, Field(max_length=255, min_length=2)]
    domain: str
    password: str

    @field_validator("domain")
    @classmethod
    def validate_domain(cls, value):
        validate_domain(value)
        return value

    @model_validator(mode="after")
    def validate_password(self):
        password = self.password
        if password:
            validate_password(password)
        return self

class CreateClientOutbound(BaseModel):
    id: int
    name: str
    domain: str

class UpdateClientInbound(BaseModel):
    name: Optional[Annotated[str, Field(max_length=255, min_length=2)]] = None
    password: Optional[str] = None
    domain: Optional[str] = None
    
    @field_validator("domain")
    @classmethod
    def validate_domain(cls, value):
        return validate_domain(value)
    
    @model_validator(mode="after")
    def validate_password(self):
        password = self.password
        if password:
            validate_password(password)
        return self