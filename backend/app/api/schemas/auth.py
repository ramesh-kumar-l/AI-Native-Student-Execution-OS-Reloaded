import uuid
from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, description="Password must be at least 6 characters")
    full_name: str = Field(min_length=1, description="Full name must not be empty")

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class GoogleLogin(BaseModel):
    id_token: str

class TokenRefresh(BaseModel):
    refresh_token: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    full_name: str
    role: str
    avatar_url: str | None = None
    email_verified: bool

    class Config:
        from_attributes = True

class RegisterResponse(BaseModel):
    id: uuid.UUID
    email: str
    full_name: str
    email_verified: bool
    message: str
