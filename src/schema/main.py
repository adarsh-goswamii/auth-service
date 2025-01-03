from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from src.schema.user import User
from src.schema.client import Client
from src.schema.application import Application