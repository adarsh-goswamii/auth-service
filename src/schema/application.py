from datetime import datetime

from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR

from src.configs.db_constants import DBTables, DBConfig
from src.schema.main import Base


class Application(Base):
    __tablename__ = DBTables.APPLICATION
    __table_args__ = {'schema': DBConfig.SCHEMA_NAME}

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    client_id = Column(BIGINT, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.CLIENT}.id'), nullable=False)
    domain = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    application_id = Column(VARCHAR(255), default=None)
    application_secret = Column(VARCHAR(255), default=None)
    public_key = Column(VARCHAR(255), default=None)
    private_key = Column(VARCHAR(255), default=None)
    added_at = Column(DateTime, default=datetime.utcnow())