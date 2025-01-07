import base64
from datetime import datetime
from fastapi import Request

from src.configs.constants import JWTExpirationTime
from src.lib.jwt import jwt_token

from src.configs.error_constants import ErrorMessages
from src.db.session import get_db, select_first, delete
from src.schema.application import Application
from src.services.oauth.serializer import GetAccessTokenInbound
from src.schema.auth_code import AuthorisationCode
from src.utils.response import error_response, success_response
from cryptography.hazmat.primitives import serialization

class OauthController:
    @classmethod
    async def get_access_token(cls, request: Request, payload: GetAccessTokenInbound):
        authorisation_data = request.headers.get('authorization')
        authorisation_data = base64.b64decode(authorisation_data).decode("utf-8")
        application_id, application_secret = authorisation_data.split(":")

        db = get_db()
        application_query = db.query(Application).filter(
            Application.application_id == application_id and Application.application_secret == application_secret)
        application = select_first(application_query)

        if not application:
            return error_response(message=ErrorMessages.NO_APPLICATION_WITH_GIVEN_ID_OR_SECRET_EXITS)

        auth_code_query = db.query(AuthorisationCode).filter(AuthorisationCode.code == payload.authorisation_code)
        auth_code = select_first(auth_code_query)

        if not auth_code or datetime.utcnow() > auth_code.expires_at:
            return error_response(message=ErrorMessages.AUTHORISATION_CODE_EXPIRED)

        private_key = application.private_key
        private_key_bytes = private_key.encode("utf-8")

        # Use the cryptography library to load the private key
        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=None
        )

        access_token = jwt_token.generate_jwt(private_key=private_key,
                                        data={"name": auth_code.user.name, "email": auth_code.user.email},
                                        expiration_minutes=JWTExpirationTime.access_token_expiration)

        refresh_token = jwt_token.generate_jwt(private_key=private_key,
                                         data={},
                                         expiration_minutes=JWTExpirationTime.refresh_token_expiration)

        delete(auth_code)
        return success_response(data={"access_token": access_token, "refresh_token": refresh_token})
