from fastapi import HTTPException, status

class AppException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

class DatabaseException(AppException):
    def __init__(self, detail: str = "Database operation failed"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

class UserAlreadyExistsException(AppException):
    def __init__(self, detail: str = "User with this email already exists"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class InvalidCredentialsException(AppException):
    def __init__(self, detail: str = "Invalid email or password"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

class TokenExpiredException(AppException):
    def __init__(self, detail: str = "Authentication token has expired"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

class InvalidTokenException(AppException):
    def __init__(self, detail: str = "Invalid authentication token"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

class EmailNotVerifiedException(AppException):
    def __init__(self, detail: str = "Please verify your email before logging in"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
