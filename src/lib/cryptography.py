from secrets import token_urlsafe

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os
import base64

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


class Cryptography:
    @classmethod
    def generate_rsa_keys(cls):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048  # Key size in bits
        )

        # Serialize the private key to PEM format
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()  # No password protection
        )

        # Generate the public key from the private key
        public_key = private_key.public_key()

        # Serialize the public key to PEM format
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return private_pem, public_pem

    @classmethod
    def generate_application_secret(cls, length: int = 32, salt_length: int = 16):
        salt = os.urandom(salt_length)  # Generate a secure random salt
        kdf = Scrypt(
            salt=salt,
            length=length,
            n=2 ** 14,  # Work factor
            r=8,  # Block size
            p=1,  # Parallelization factor
            backend=default_backend(),
        )
        secret_key = kdf.derive(os.urandom(16))  # Derive a key
        return base64.urlsafe_b64encode(secret_key).decode("utf-8")

    @classmethod
    def generate_random_string(cls, length: int = 16):
        return token_urlsafe(length)


cryptography = Cryptography()
