from datetime import datetime, timedelta

from src.configs.env import get_settings
from src.configs.error_constants import ErrorMessages
from src.db.session import get_db, save_new_row, delete, select_first
from src.lib.bcrypt import bcrypt
from src.lib.cryptography import cryptography
from src.schema.auth_code import AuthorisationCode
from src.services.user.serializer import CreateUserInbound, CreateUserOutbound, DeleteUserInbound
from src.schema.user import User
from src.utils.response import success_response, error_response

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


