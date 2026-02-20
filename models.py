from datetime import datetime, timezone
from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__: str = "users"  # type: ignore

    userid: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(min_length=3, max_length=50, unique=True)
    email: EmailStr = Field(unique=True)
    passwordhash: str
    createdat: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class UserCreate(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    passwordhash: str
