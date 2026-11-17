from dotenv import load_dotenv
import os

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "drivername": "postgresql+psycopg"
}

url = URL.create(**DB_CONFIG)

engine = create_engine(url) #  echo=True)

Session = sessionmaker(bind=engine)