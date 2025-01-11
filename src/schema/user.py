from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from sqlalchemy.orm import relationship

from src.configs.db_constants import DBTables, DBConfig
from .main import Base

class User(Base):
    __tablename__ = DBTables.USER
    __table_args__ = {'schema': DBConfig.SCHEMA_NAME}

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    password = Column(VARCHAR(100), nullable=False)

    authorisation_codes = relationship('AuthorisationCode', back_populates='user')
    refresh_tokens = relationship('RefreshToken', back_populates="user")

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }