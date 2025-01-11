import base64
from datetime import datetime, timedelta
from fastapi import Request
from starlette.responses import JSONResponse

from src.configs.constants import JWTExpirationTime
from src.lib.bcrypt import bcrypt
from src.lib.cryptography import cryptography
from src.lib.jwt import jwt_token

from src.configs.error_constants import ErrorMessages
from src.db.session import get_db, select_first, delete, save_new_row
from src.schema.application import Application
from src.schema.session import Session
from src.schema.user import User
from src.services.oauth.serializer import GetAccessTokenInbound, LoginUserInbound
from src.schema.auth_code import AuthorisationCode
from src.utils.response import error_response, success_response
from cryptography.hazmat.primitives import serialization


class OauthController:
    @classmethod
    async def login_user(cls, request: Request, payload: LoginUserInbound):
        db = get_db()
        query = db.query(User).filter(User.email == payload.email)
        user = select_first(query)

        if not user:
            return error_response(ErrorMessages.NO_USER_WITH_GIVEN_EMAIL_EXITS)

        is_pass_correct = bcrypt.verify_str(payload.password, user.password)

        if not is_pass_correct:
            return error_response(ErrorMessages.INCORRECT_PASSWORD)

        auth_query = db.query(AuthorisationCode).filter(AuthorisationCode.user_id == user.id)
        existing_auth_code = select_first(auth_query)

        if existing_auth_code:
            delete(existing_auth_code)

        authorisation_code = cryptography.generate_random_string()
        session_id = cryptography.generate_random_string()
        authorisation_code_expires_at = datetime.utcnow().replace(microsecond=0) + timedelta(minutes=10)
        session_id_expires_at = datetime.utcnow().replace(microsecond=0) + timedelta(hours=12)
        ip_address = request.client.host
        user_agent = request.headers.get('user_agent', 'Unknown')

        auth_code = AuthorisationCode(code=authorisation_code, user_id=user.id,
                                      expires_at=authorisation_code_expires_at)
        session = Session(user_id=user.id, session_id=session_id, ip_address=ip_address, user_agent=user_agent,
                          expires_at=session_id_expires_at)

        save_new_row(auth_code)
        save_new_row(session)

        response = JSONResponse(content={"authorisation_code": authorisation_code})
        response.set_cookie(key='session_id', value=session_id, httponly=True, max_age=12 * 60 * 60)
        return response

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
