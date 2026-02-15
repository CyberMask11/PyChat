from fastapi import FastAPI, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.util.init_db import create_tables
from contextlib import asynccontextmanager
from app.router.auth import route
from app.router.chat import api
from app.service.userService import UserService
from app.db.schema.user import UserInOutput
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route, tags=["Authentication"], prefix="/auth")
app.include_router(api, tags=["WebChat"], prefix='/chat')

@app.get('/users', status_code=200, response_model=list[UserInOutput])
def get_users(
    displayname: str,
    session: Session = Depends(get_db)
):
    return UserService(session=session).GetUsers(displayname)
