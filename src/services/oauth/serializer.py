from pydantic import BaseModel


class GetAccessTokenInbound(BaseModel):
    authorisation_code: str