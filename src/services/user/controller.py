from datetime import datetime, timedelta

from configs.env import get_settings
from configs.error_constants import ErrorMessages
from db.session import get_db, save_new_row, delete, select_first
from lib.bcrypt import bcrypt
from lib.cryptography import cryptography
from lib.jwt import jwt
from schema.auth_code import AuthorisationCode
from services.user.serializer import CreateUserInbound, CreateUserOutbound, DeleteUserInbound, LoginUserInbound
from src.schema.user import User
from utils.response import success_response, error_response

config = get_settings()


class UserController:

    @classmethod
    async def create_user(cls, request, payload: CreateUserInbound):
        db = get_db()
        query = db.query(User).filter(User.email == payload.email)
        existing_user = select_first(query)

        if existing_user:
            return error_response(message=ErrorMessages.EMAIL_ALREADY_EXISTS)

        encoded_password = bcrypt.encode_str(payload.password)
        new_user = User(name=payload.name, email=payload.email, password=encoded_password)
        new_user = save_new_row(new_user)

        return CreateUserOutbound(**new_user.dict())

    @classmethod
    async def delete_user(cls, request, payload: DeleteUserInbound):
        db = get_db()
        query = db.query(User).filter(User.email == payload.email)

        user = select_first(query)
        return delete(user)

    @classmethod
    async def update_user(cls, request, payload):
        # add password reset logic here.
        pass

    @classmethod
    async def validate_user(cls, request, payload: LoginUserInbound):
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
        expires_at = datetime.utcnow().replace(microsecond=0) + timedelta(minutes=10)

        print(expires_at)

        auth_code = AuthorisationCode(code=authorisation_code, user_id=user.id,
                                      expires_at=expires_at)
        save_new_row(auth_code)

        return success_response({"authorisation_code": authorisation_code})
