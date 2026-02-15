from fastapi import HTTPException, Depends, Header, status
from sqlalchemy.orm import Session
from typing import Annotated
from app.core.database import get_db
from app.service.userService import UserService
from app.db.schema.user import UserInOutput
from app.core.security.authHandler import AuthHandler

PREFIX = 'Bearer '

def current_user(
        session: Session = Depends(get_db),
        authorization: Annotated[str | None, Header()] = None
) -> UserInOutput:
    auth_except = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    if not authorization:
        raise auth_except
    
    if not authorization.startswith(PREFIX):
        raise auth_except
    
    payload = AuthHandler.decode_jwt(authorization[len(PREFIX):])

    if payload and payload["user_id"]:
        user = UserService(session=session).get_user_by_id(user_id=payload["user_id"])
        return UserInOutput(
            id=user.id,
            displayname=user.displayname
        )
    raise auth_except