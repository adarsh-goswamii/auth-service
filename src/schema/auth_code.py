from datetime import datetime

from sqlalchemy import Column, BIGINT, VARCHAR, DateTime, Integer, ForeignKey

from configs.db_constants import DBTables, DBConfig
from schema.main import Base


class AuthorisationCode(Base):
    __tablename__ = DBTables.AUTHORISATION_CODE
    __table_args__ = { "schema": DBConfig.SCHEMA_NAME }

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    code = Column(VARCHAR(32), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.USER}.id'), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    # client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    # scope = Column(String(255), nullable=True)

class Application(Base):
    __tablename__ = DBTables.APPLICATION
    __table_args__ = {'schema': DBConfig.SCHEMA_NAME}

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    client_id = Column(BIGINT, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.CLIENT}.id'), nullable=False)
    domain = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    application_id = Column(VARCHAR(255), default=None)
    application_secret = Column(VARCHAR(255), default=None)
    public_key = Column(VARCHAR(5000), default=None)
    private_key = Column(VARCHAR(5000), default=None)
    added_at = Column(DateTime, default=datetime.utcnow())

    def dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "domain": self.domain,
            "name": self.name,
            "application_id": self.application_id,
            "application_secret": self.application_secret,
            "public_key": self.public_key,
            "private_key": self.private_key,
            "added_at": self.added_at
        }

class Client(Base):
    __tablename__ = DBTables.CLIENT
    __table_args__ = {'schema': DBConfig.SCHEMA_NAME}

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    domain =  Column(VARCHAR(255), nullable=False, index=True)
    password = Column(VARCHAR(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

class User(Base):
    __tablename__ = DBTables.USER
    __table_args__ = {'schema': DBConfig.SCHEMA_NAME}

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    password = Column(VARCHAR(100), nullable=False)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }