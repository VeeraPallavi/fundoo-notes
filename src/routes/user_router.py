from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from loguru import logger

from src.utils.dependency import get_db
from src.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from src.models.user import User
from src.services.user_service import *
router = APIRouter()

# CREATE USER
@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

# GET ALL USERS
@router.get("/", response_model=list[UserResponse])
def get(db: Session = Depends(get_db)):

   return get_users(db)


# GET USER BY ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):

    return get_user(user_id,db)


# UPDATE USER
@router.put("/{user_id}", response_model=UserResponse)
def update(updated_user: UserUpdate, db: Session = Depends(get_db)):

    return update_user(updated_user,db)


# DELETE USER
@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):

    return delete_user(user_id,db)

    