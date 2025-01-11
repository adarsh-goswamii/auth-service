from pydantic import BaseModel, EmailStr


class GetAccessTokenInbound(BaseModel):
    authorisation_code: str

class LoginUserInbound(BaseModel):
    email: EmailStr
    password: str

class RefreshTokenInbound(BaseModel):
    refresh_token: str
    application_id: str