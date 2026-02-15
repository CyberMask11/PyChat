from decouple import config
import time
import jwt
import uuid

SECRET = config("SECRET_JWT")
ALGORITHM = config("ALGORITHM_JWT")

class AuthHandler:
    @staticmethod
    def sign_jwt(user_id: uuid.UUID):
        payload = {
            "user_id": str(user_id),
            "expires": time.time() + 3600
        }

        token = jwt.encode(payload, SECRET, ALGORITHM)
        return token
    
    @staticmethod
    def decode_jwt(token: str):
        decoded_token = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        try:
            return decoded_token if decoded_token["expires"] >= time.time() else None
        except:
            return None