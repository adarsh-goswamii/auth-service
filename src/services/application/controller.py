import base64
from uuid import uuid4
from sqlalchemy import and_
from fastapi import Request

from src.configs.error_constants import ErrorMessages
from src.lib.cryptography import cryptography
from src.schema.client import Client
from src.schema.application import Application
from src.db.session import get_db, select_first, save_new_row
from src.services.application.serializer import AddApplicationInbound, AddApplicationOutbound
from src.utils.common import remove_pem_headers
from src.utils.response import error_response, success_response


class ApplicationController:
    @classmethod
    async def add_application(cls, request: Request, payload: AddApplicationInbound):
        db = get_db()
        client_query = db.query(Client).filter(Client.id == payload.client_id)
        client = select_first(client_query)
        if client.domain not in payload.domain:
            return error_response(message=ErrorMessages.APPLICATION_NOT_A_SUBDOMAIN)

        app_query = db.query(Application).filter(
            and_(Application.client_id == payload.client_id, Application.domain == payload.domain))
        existing_app = select_first(app_query)

        if existing_app:
            return error_response(message=ErrorMessages.APPLICATION_ALREADY_EXISTS)

        private_key_pem, public_key_pem = cryptography.generate_rsa_keys()
        private_key, public_key = private_key_pem.decode("utf-8"), public_key_pem.decode("utf-8")
        application_id = uuid4()
        application_secret = cryptography.generate_application_secret()

        application = Application(client_id=client.id, domain=payload.domain, name=payload.name,
                                  application_id=application_id, application_secret=application_secret,
                                  public_key=public_key, private_key=private_key)

        application = save_new_row(application)

        return success_response(AddApplicationOutbound(**application.dict()))
