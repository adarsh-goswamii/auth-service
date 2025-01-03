from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR

from configs.db_constants import DBTables, DBConfig
from src.schema.main import Base

class User(Base):
    __tablename__ = DBTables.USER
    __table_args__ = {'schema': DBConfig.SCHEMA_NAME}

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    password = Column(VARCHAR(100), nullable=False)