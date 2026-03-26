import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

username = os.getenv("username")
password = quote_plus(os.getenv("password"))
server = os.getenv("server")
database = os.getenv("database")

DATABASE_URL = "mssql+pyodbc://@DESKTOP-P8GCKCP\\SQLEXPRESS/FundooAPPdb?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()