from passlib.context import CryptContext

class Bcrypt:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def encode_str(cls, value: str):
        return cls.pwd_context.hash(value)

    @classmethod
    def verify_str(cls, value: str, encoded_value: str):
        return cls.pwd_context.verify(value, encoded_value)


bcrypt = Bcrypt()