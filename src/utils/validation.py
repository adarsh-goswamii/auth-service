def validate_password(password: str) -> None:
    length = len(password)
    if length <8 or length >100:
        raise ValueError("Password should be 8-100 character long.")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char in "@$!%*?&" for char in password):
        raise ValueError("Password must contain at least one special character (@$!%*?&).")
