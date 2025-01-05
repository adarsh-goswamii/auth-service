from db.session import get_db, save_new_row, delete, select_first
from lib.bcrypt import bcrypt
from services.user.serializer import CreateUserInbound, CreateUserOutbound, DeleteUserInbound
from src.schema.main import User


class UserController:

    @classmethod
    async def create_user(cls, request, payload: CreateUserInbound):
        encoded_password = bcrypt.encode_str(payload.password)
        new_user = User(name=payload.name, email=payload.email, password=encoded_password)
        new_user = save_new_row(new_user)

        return CreateUserOutbound(**new_user.dict())

    @classmethod
    async def delete_user(cls, request, payload: DeleteUserInbound):
        db = get_db()
        query = db.query(User).filter(User.email==payload.email)

        user = select_first(query)
        return delete(user)

    @classmethod
    async def update_user(cls, request, payload):
        # add password reset logic here.
        pass

    @classmethod
    async def validate_user(cls, request, payload):
        pass
