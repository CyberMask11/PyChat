from pydantic import BaseModel
from uuid import UUID

class UserInCreate(BaseModel):
    displayname: str
    username: str
    password: str

class UserInLogin(BaseModel):
    username: str
    password: str

class UserInOutput(BaseModel):
    id: UUID
    displayname: str

    class Config:
        from_attributes = True

class UserToken(BaseModel):
    token: str

class UserUpdate(BaseModel):
    displayname: str | None = None
    username: str | None = None
    password: str | None = None