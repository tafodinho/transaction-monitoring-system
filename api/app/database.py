from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from starlette.config import Config
from starlette.datastructures import Secret

config = Config("../../.env")

DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default="barister")
DB_USER = config("DB_USER", default="postgres")
DB_SERVER = config("DB_SERVER", cast=str, default="db")
DB_NAME = config("DB_NAME", cast=str, default="TMS")
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()