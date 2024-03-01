# pip install sqlalchemy
# pip install psycopg2
# pip install python-dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import os
# from dotenv import load_dotenv
# load_dotenv()

from sql_app.db_url import SQLALCHEMY_DATABASE_URL

## For sqlite

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

## For postgresql
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRESQL_URL")
# SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRESQL_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


conn = engine.connect()
print(conn.get_isolation_level())