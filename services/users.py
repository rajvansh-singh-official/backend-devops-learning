from pydantic import BaseModel, EmailStr
from database import SessionLocal
from models.user import User

class UserCreate(BaseModel):
    name: str
    email: EmailStr

def get_users():
    db = SessionLocal()
    
    try:
        return db.query(User).all()
    
    finally:
        db.close()

def create_user(user: UserCreate):
    db = SessionLocal()

    try:
        db_user = User(
            name=user.name,
            email=user.email
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    finally:
        db.close()

def get_user_by_id(user_id: int):
    db = SessionLocal()
    
    try:
        return db.query(User).filter(User.id == user_id).first()
    
    finally:
        db.close()

def update_user(user_id: int, name: str | None = None, email: str | None = None):
    db = SessionLocal()
    
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return None

        if name is not None:
            user.name = name
        if email is not None:
            user.email = email

        db.commit()
        db.refresh(user)
        return user
    
    finally:
        db.close()


def delete_user(user_id: int):
    db = SessionLocal()
    
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return None

        db.delete(user)
        db.commit()
        return user
    
    finally:
        db.close()