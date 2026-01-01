from fastapi import FastAPI, HTTPException
from services.users import (
  get_users,
  create_user, 
  UserCreate, 
  get_user_by_id, 
  update_user, 
  delete_user
)
from schemas.users import UserResponse
from models.user import User
from database import engine, Base
from typing import Optional

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
  return{"message": "API running"}

@app.get("/health")
def health_check():
  return {"status": "ok"}

@app.get("/users", response_model=list[UserResponse])
def list_users():
    return get_users()

@app.post("/users", response_model=UserResponse)
def add_user(user: UserCreate):
    created_user = create_user(user)
    if created_user is None:
        raise HTTPException(status_code=409, detail="Email already exists")
    return created_user

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.patch("/users/{user_id}", response_model=UserResponse)
def update_user_route(
    user_id: int,
    name: Optional[str] = None,
    email: Optional[str] = None
):
    user = update_user(user_id, name, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}", response_model=UserResponse)
def delete_user_route(user_id: int):
    user = delete_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user