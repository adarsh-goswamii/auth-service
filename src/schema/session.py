from datetime import datetime

from sqlalchemy import Column, BIGINT, VARCHAR, DateTime, ForeignKey

from src.configs.db_constants import DBTables, DBConfig
from .main import Base

class Session(Base):
    __tablename__ = DBTables.SESSION
    __table_args__ = {'schema': DBConfig.SCHEMA_NAME}

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    user_id =  Column(BIGINT, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.USER}.id'))
    session_id =  Column(VARCHAR(100), nullable=False, unique=True)
    ip_address = Column(VARCHAR(100), nullable=False)
    user_agent = Column(VARCHAR(100), nullable=False)
    expires_at = Column(DateTime, nullable=False)

