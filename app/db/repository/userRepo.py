from .base import BaseRepo
from app.db.schema.user import UserInCreate, UserInOutput
from app.db.model.users import Users
from sqlalchemy.dialects.postgresql import UUID

class UserRepo(BaseRepo):
    def create_user(self, userDetails: UserInCreate):
        user = Users(**userDetails.model_dump(exclude_none=True))

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user
    
    def get_user_by_displayname(self, username: str) -> UserInOutput:
        user = self.session.query(Users).filter(Users.displayname==username).first()
        return user
    
    def get_user_by_id(self, user_id: UUID) -> Users:
        user = self.session.query(Users).filter(Users.id==user_id).first()
        return user
    
    def get_user_by_username(self, username: str) -> Users:
        user = self.session.query(Users).filter(Users.username==username).first()
        return user
    
    def user_exist_by_username(self, username: str) -> bool:
        user = self.session.query(Users).filter(Users.username==username).first()
        return bool(user)
    
    def user_exist_by_displayname(self, name: str) -> bool:
        user = self.session.query(Users).filter(Users.displayname==name).first()
        return bool(user)
    
    def display_users(self, displayname: str, limit: int = 10, offset: int = 0) -> list[Users]:
        return (
            self.session.query(Users)
            .filter(Users.displayname.ilike(f"%{displayname}%"))
            .limit(limit)
            .offset(offset)
            .all()
        )