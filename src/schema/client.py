from datetime import datetime

from sqlalchemy import Column, BIGINT, VARCHAR, DateTime

from src.configs.db_constants import DBTables, DBConfig
from .main import Base

class Client(Base):
    __tablename__ = DBTables.CLIENT
    __table_args__ = {'schema': DBConfig.SCHEMA_NAME}

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    domain =  Column(VARCHAR(255), nullable=False, index=True)
    password = Column(VARCHAR(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

