from uuid import uuid4

from fastapi import Request

from configs.error_constants import ErrorMessages
from lib.cryptography import cryptography
from src.schema.main import Client, Application
from db.session import get_db, select_first, save_new_row
from services.application.serializer import AddApplicationInbound, AddApplicationOutbound
from utils.response import error_response, success_response


class ApplicationController:
    @classmethod
    async def add_application(cls, request: Request, payload: AddApplicationInbound):
        db = get_db()
        client_query = db.query(Client).filter(Client.id == payload.client_id)
        client = select_first(client_query)
        if client.domain not in payload.domain:
            return error_response(message=ErrorMessages.APPLICATION_NOT_A_SUBDOMAIN)

        app_query = db.query(Application).filter(
            Application.client_id == payload.client_id and Application.domain == payload.domain)
        existing_app = select_first(app_query)

        if existing_app:
            return error_response(message=ErrorMessages.APPLICATION_ALREADY_EXISTS)

        private_key, public_key = cryptography.generate_rsa_keys()
        application_id = uuid4()
        application_secret = cryptography.generate_application_secret()

        application = Application(client_id=client.id, domain=payload.domain, name=payload.name,
                                  application_id=application_id, application_secret=application_secret,
                                  public_key=public_key, private_key=private_key)

        application = save_new_row(application)

        return success_response(AddApplicationOutbound(**application.dict()))
