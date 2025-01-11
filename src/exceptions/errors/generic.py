from src.configs.error_constants import ErrorMessages


class JWTExpiredTokenException(Exception):
  def __init__(self, message=ErrorMessages.TOKEN_HAS_EXPIRED):
    self.message = message
    super().__init__(self.message)


class JWTInvalidTokenException(Exception):
  def __init__(self, message=ErrorMessages.INVALID_TOKEN):
    self.message = message
    super().__init__(self.message)

