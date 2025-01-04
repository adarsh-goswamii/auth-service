from db.session import get_db, save_new_row
from lib.bcrypt import bcrypt
from services.user.serializer import CreateUserInbound
from src.schema.main import User


class UserController:

    @classmethod
    async def create_user(cls, request, payload: CreateUserInbound):
        encoded_password = bcrypt.encode_str(payload.password)
        new_user = User(name=payload.name, email=payload.email, password=encoded_password)
        new_user = save_new_row(new_user)

        return new_user

    @classmethod
    async def delete_user(cls, request, payload):
        pass

    @classmethod
    async def update_user(cls, request, payload):
        pass

    @classmethod
    async def validate_user(cls, request, payload):
        pass
