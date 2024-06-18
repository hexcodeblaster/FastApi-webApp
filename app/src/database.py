from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy .ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

DATABASE_URL = "postgresql://postgres:password@localhost/postgres"

engine = create_engine(os.getenv("DATABASE_URL", DATABASE_URL))

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()
