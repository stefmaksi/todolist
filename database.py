import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL found. Check your .env file!")

engine = create_engine(DATABASE_URL, echo=True)


# This Dependency safely opens/closes the database connection
def get_session():
    with Session(engine) as session:
        yield session
