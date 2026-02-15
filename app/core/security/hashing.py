from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashing(password: str) -> str:
    return context.hash(password[:72])

def verify(password: str, encrypted_pwd: str) -> bool:
    return context.verify(password, encrypted_pwd)