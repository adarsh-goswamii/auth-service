from sqlalchemy import Column, BIGINT, VARCHAR, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.configs.db_constants import DBTables, DBConfig
from .main import Base


class RefreshToken(Base):
    __tablename__ = DBTables.REFRESH_TOKEN
    __table_args__ = { "schema": DBConfig.SCHEMA_NAME }

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    token = Column(VARCHAR(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.USER}.id'), nullable=False)
    application_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.APPLICATION}.id'), nullable=False)
    issued_at = Column(DateTime, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    revoked = Column(Boolean, default=False, nullable=False)

    application = relationship('Application', back_populates='refresh_tokens')
    user = relationship('User', back_populates="refresh_tokens")