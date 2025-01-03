from datetime import datetime

from sqlalchemy import Column, BIGINT, VARCHAR, DateTime

from configs.db_constants import DBTables
from src.schema.main import Base

class Client(Base):
    __tablename__ = DBTables.CLIENT

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    domain =  Column(VARCHAR(255), nullable=False, index=True)
    password = Column(VARCHAR(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
