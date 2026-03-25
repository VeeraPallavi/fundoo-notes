from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer,Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    contact_no = Column(String(15))
    is_active = Column(Boolean, default=False)
    