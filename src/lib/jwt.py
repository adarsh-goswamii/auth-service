from datetime import datetime, timedelta
import jwt
from jwt import ExpiredSignatureError

from src.configs.error_constants import ErrorMessages
from src.exceptions.errors.generic import JWTExpiredTokenException, JWTInvalidTokenException


class JWT:
    @classmethod
    def generate_jwt(cls, private_key: str, data: dict, expiration_minutes: int):
        expiration = datetime.utcnow() + timedelta(minutes=expiration_minutes)
        payload = {**data, "exp": expiration}

        token = jwt.encode(payload, private_key, algorithm="RS256")
        return token

    @classmethod
    def decode_token(cls, public_key: str, token: str):
        try:
            return jwt.decode(jwt=token, key=public_key, algorithms="RS256")
        except ExpiredSignatureError:
            raise JWTExpiredTokenException()
        except jwt.DecodeError:
            raise JWTInvalidTokenException()


jwt_token = JWT()