# From .env file
import os

from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import sessionmaker


class Database:
  def __init__(self):
    self.DB_ADDRESS = os.getenv("DB_ADDRESS")
    self.DB_PORT = os.getenv("DB_PORT")
    self.DB_USER = os.getenv("DB_USER")
    self.DB_PASSWORD = os.getenv("DB_PASSWORD")
    self.DB_NAME = os.getenv("DB_NAME")
    if not all([self.DB_ADDRESS, self.DB_PORT, self.DB_USER, self.DB_PASSWORD, self.DB_NAME]):
      raise ValueError("Database configuration is not complete.")
    
    self.DSN = f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_ADDRESS}:{self.DB_PORT}/{self.DB_NAME}"
    self.engine = create_engine(self.DSN)
    self.SessionLocal = sessionmaker(
      autocommit=False, 
      autoflush=False, 
      bind=self.engine
    )
  def create_db_and_tables(self):
    SQLModel.metadata.create_all(self.engine)

  def get_session(self):
    return self.SessionLocal()

    # def get_session(self):
    #   return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)()
