from pydantic import BaseModel, EmailStr

users = []

class UserCreate(BaseModel):
    name: str
    email: EmailStr

def get_users():
    return users

def create_user(user: UserCreate):
    new_user = {
        "id": len(users) + 1,
        "name": user.name
    }
    users.append(new_user)
    return new_user

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