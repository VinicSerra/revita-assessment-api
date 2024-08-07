from sqlalchemy import create_engine
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Annotated

DB_CONNECTION_STRING = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"

engine = create_engine(
    DB_CONNECTION_STRING,pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
Database = Annotated[Session, Depends(get_db)]