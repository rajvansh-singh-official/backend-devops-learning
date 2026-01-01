from pydantic import BaseModel, EmailStr
from database import SessionLocal
from models.user import User

users = []

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
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def update_user(user_id: int, name: str | None = None, email: str | None = None):
    for user in users:
        if user["id"] == user_id:
            if name is not None:
                user["name"] = name
            if email is not None:
                user["email"] = email
            return user
    return None


def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            return users.pop(i)
    return None