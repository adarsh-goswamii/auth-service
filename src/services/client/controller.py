from db.session import get_db, save_new_row, delete, select_first
from lib.bcrypt import bcrypt
from services.client.serializer import CreateClientInbound, CreateClientOutbound
from src.schema.main import Client


class ClientController:

    @classmethod
    async def create_client(cls, request, payload: CreateClientInbound):
        encoded_password = bcrypt.encode_str(payload.password)
        new_client = Client(name=payload.name, password=encoded_password, domain=payload.domain)
        new_client = save_new_row(new_client)

        return CreateClientOutbound(**new_client.dict())

    @classmethod
    async def delete_client(cls, request, payload):
        db = get_db()
        query = db.query(Client).filter(Client.domain==payload.domain)

        client = select_first(query)
        return delete(client)

    @classmethod
    async def update_client(cls, request, payload):
        # add password reset logic here.
        pass

    @classmethod
    async def validate_client(cls, request, payload):
        pass
