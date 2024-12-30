from pydantic import BaseSettings

class Settings(BaseSettings):
  # Define env variables here.
  
  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"
    
setting = Settings()