
from fastapi import FastAPI
from src.models.user import Base
from src.Config.database import engine
from src.routes.user_router import router

app = FastAPI()

# CREATE TABLES
Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/users", tags=["Users"])
