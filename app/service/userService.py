from fastapi import HTTPException
from app.core.security.authHandler import AuthHandler
from app.core.security.hashing import hashing, verify
from app.db.schema.user import UserInCreate,UserInLogin,UserInOutput,UserToken
from app.db.repository.userRepo import UserRepo
from sqlalchemy.orm import Session
import uuid

class UserService:
    def __init__(self, session: Session):
        self.__userRepo = UserRepo(session=session)

    def SignUp(self, UserDetails: UserInCreate) -> UserInOutput:
        if self.__userRepo.user_exist_by_displayname(UserDetails.displayname):
            raise HTTPException(status_code=400, detail="User displayname already exist.")
        
        if not UserDetails.displayname.startswith("@"):
            raise HTTPException(status_code=422, detail="Displayname must start with @.")

        if self.__userRepo.user_exist_by_username(UserDetails.username):
            raise HTTPException(status_code=400, detail="User already exist.")
        
        hashed_pwd = hashing(UserDetails.password)
        UserDetails.password = hashed_pwd
        return self.__userRepo.create_user(userDetails=UserDetails)
    
    def Login(self, UserDetails: UserInLogin) -> UserToken:
        if not self.__userRepo.user_exist_by_username(UserDetails.username):
            raise HTTPException(status_code=404, detail="User does not exist.")

        user = self.__userRepo.get_user_by_username(UserDetails.username)
        verify_user = verify(UserDetails.password, user.password)

        if verify_user:
            token = AuthHandler.sign_jwt(user.id)
            if token:
                return UserToken(token=token)
            raise HTTPException(status_code=500, detail="Unable to generate token.")
        raise HTTPException(status_code=500, detail="User not verified.")
    
    def GetUsers(self, displayname: str) -> UserInOutput:
        if self.__userRepo.user_exist_by_displayname:
            return self.__userRepo.display_users(displayname)
        return None
    
    def get_user_with_id(self, user_id: uuid.UUID):
        return self.__userRepo.get_user_by_id(user_id)