from datetime import datetime, timedelta
import jwt

class JWT:
    @classmethod
    def generate_jwt(cls, private_key: str, data: dict, expiration_minutes: int):
        print(private_key)
        expiration = datetime.utcnow() + timedelta(minutes=expiration_minutes)
        payload = {**data, "exp": expiration}

        token = jwt.encode(payload, private_key, algorithm="RS256")
        return token

jwt_token = JWT()