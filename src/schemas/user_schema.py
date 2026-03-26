from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
   name : str
   password : str = Field(min_length=5)
   email : EmailStr
   contact_no : str
   

class UserResponse(BaseModel):
   id : int 
   name : str
   email: EmailStr
   contact_no : str
   is_active : bool

   class Config :
      from_attributes = True

class UserUpdate(BaseModel):
    id : int 
    name : str
    email: EmailStr
    password : str = Field(min_length=5)
    contact_no : str
    is_active : bool

    class Config :
        from_attributes = True