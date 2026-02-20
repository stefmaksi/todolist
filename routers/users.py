from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

# Import our stuff from the other files!
from database import get_session
from models import User, UserCreate

# Create the router.
# We add prefix="/users" so we don't have to type it on every single route!
router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{username}")
def get_user(username: str, session: Session = Depends(get_session)):
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/")
def create_user(user_input: UserCreate, session: Session = Depends(get_session)):
    db_user = User.model_validate(user_input)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user
