from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from src.Config.logger import logger

from src.utils.dependency import get_db
from src.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from src.models.user import User


def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:

    try:
        logger.info("Creating user:")
        new_user = User(
            name=user.name,
            email=user.email,
            password=user.password,
            contact_no=user.contact_no
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        logger.info("User created successfully",
                    extra = {"name":new_user.name,"email": new_user.email})

        return new_user

    except IntegrityError as e:
        db.rollback()
        logger.error("Integrity error creating user",
                     extra ={"email ": user.email})
        raise HTTPException(status_code=400, detail="User with same email already exists")
    
    except Exception as e:
        db.rollback()
        logger.error(
            "Database error creating user",
            extra = {"email":user.email}
        )
        raise HTTPException(status_code = 500, details = "Internal Server error")
    
def get_users(db: Session = Depends(get_db)) -> list[User]:
    try :
        logger.info("Fetching all users")
        return db.query(User).all()

    except SQLAlchemyError as e :
        logger.error("Failed to fetch all the details")
        raise HTTPException(status_code = 500, details = "Internal Server Error")

def get_user(user_id: int, db: Session = Depends(get_db))->User:

    try :
        logger.info(f"Fetching user by id :{user_id}")
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            logger.warning("User not found",
                           extra ={"user_id":user_id})
            
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except SQLAlchemyError as e:
        logger.error("Failed to fetch the details")
        raise HTTPException(status_code = 500, details = "Internal Server Error")

def update_user(updated_user: UserUpdate, db: Session = Depends(get_db)) -> User:

    try: 
        logger.info(f"Updating user : {updated_user.id}")
        user = db.query(User).filter(User.id == updated_user.id).first()

        if not user:
            logger.warning(
                "User not found",
                extra={"user_id": updated_user.id}
            )
            raise HTTPException(status_code=404, detail="User not found")
        
        user.name = updated_user.name
        user.email = updated_user.email
        user.password = updated_user.password
        user.contact_no = updated_user.contact_no
        user.is_active = updated_user.is_active

        db.commit()
        db.refresh(user)
        logger.info(f"User updated successfully: {user.id}")
        return user

    except IntegrityError as e:
        db.rollback()
        logger.error(
            "Integrity error updating user",
            extra={"user_id": updated_user.id, "email": updated_user.email}
        )
        raise HTTPException(status_code=400, detail="Email already in use")
    except SQLAlchemyError as e:
        logger.error(
            "Database error updating user",
            extra={"user_id": updated_user.id}
        )
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    except Exception as e:
        logger.error(f"Some thing went wrong: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
def delete_user(user_id: int, db: Session = Depends(get_db)) -> dict:
    try:
        logger.info(f"Delete user with id : {user_id}")
        user = db.query(User).filter(User.id == user_id).first()
        
        if not user:
            logger.warning("User not found for deletion",
                           extra = {"user_id" :user_id})
            raise HTTPException(status_code=404, detail="User not found")

        db.delete(user)
        db.commit()

        logger.info("User deleted successfully")

        return {"message": "User deleted successfully"}

    except Exception as e:
        logger.exception("Error while deleting user")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")