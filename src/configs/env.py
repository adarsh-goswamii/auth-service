import os
from pydantic_settings import BaseSettings
from typing import ClassVar
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

class DBConfig:
  """
  db config
  """
  db_name: str
  db_host: str
  db_username: str
  db_password: str
  
class AppDBConfig(DBConfig):
  """
  App DB config
  """
  db_host: str = os.getenv("DB_HOST", "localhost")
  db_name: str = os.getenv("DB_NAME", "postgres")
  db_username: str = os.getenv("DB_USERNAME", "admin")
  db_password: str = os.getenv("DB_PASSWORD", "admin")
  
class BaseConfig(BaseSettings):
  """
  Base Config
  """
  env: str = os.getenv("APP_ENV", "local")
  db_app: ClassVar[DBConfig] = AppDBConfig
  

"""
lru_cache: caches the output of a function for a given input,
so for the next calls if we get the same inputs it will just give the result from the cache
"""
@lru_cache()
def get_settings():
  """
  get env
  """
  return BaseConfig()