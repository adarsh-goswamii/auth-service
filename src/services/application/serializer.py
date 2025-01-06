from typing import Annotated

from pydantic import BaseModel, Field, model_validator

from utils.validation import validate_domain


class AddApplicationInbound(BaseModel):
    client_id: int
    name: Annotated[str, Field(max_length=255, min_length=2)]
    domain: str

    @model_validator(mode="after")
    def validate_domain(self):
        domain = self.domain
        if domain:
            validate_domain(domain)
        return self

class AddApplicationOutbound(BaseModel):
    id: int
    client_id: int
    domain: str
    name: str
    application_id: str
    application_secret: str
    public_key: str
