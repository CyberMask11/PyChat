from fastapi import APIRouter, Depends
from app.db.schema.user import UserInCreate, UserInLogin, UserInOutput, UserToken
from app.service.userService import UserService
from sqlalchemy.orm import Session
from app.core.database import get_db

route = APIRouter()

@route.post('/SignUp', status_code=201, response_model=UserInOutput)
def signup(
    user_details: UserInCreate, 
    session: Session = Depends(get_db)
):
    return UserService(session=session).SignUp(user_details)

@route.post('/Login', status_code=200, response_model=UserToken)
def login(
    login_details: UserInLogin,
    session: Session = Depends(get_db)
):
    return UserService(session=session).Login(login_details)