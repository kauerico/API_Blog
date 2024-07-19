import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_HOST = os.getenv('DATABASE_HOST', 'db')
DATABASE_USER = os.getenv('DATABASE_USER', 'kaue')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '123')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'database_application')

DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
