from sqlalchemy import Column, BIGINT, VARCHAR, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.configs.db_constants import DBTables, DBConfig
from .main import Base


class AuthorisationCode(Base):
    __tablename__ = DBTables.AUTHORISATION_CODE
    __table_args__ = { "schema": DBConfig.SCHEMA_NAME }

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    code = Column(VARCHAR(32), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.USER}.id'), nullable=False)
    expires_at = Column(DateTime, nullable=False)

    user = relationship('User', back_populates='authorisation_codes')

    # client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    # scope = Column(String(255), nullable=True)