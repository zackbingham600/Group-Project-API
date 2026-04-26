from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: int
    username: str

    model_config = {"from_attributes": True}  # allows mapping from SQLAlchemy model

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    user: Optional[UserSchema] = None
    errorMessage: str = ""
    statusCode: int = 200