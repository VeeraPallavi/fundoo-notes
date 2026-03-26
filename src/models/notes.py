from src.Config.database import Base 
from sqlalchemy import Column, String, Integer, ForeignKey
from src.models.user import User

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    description = Column(String, nullable=False)

