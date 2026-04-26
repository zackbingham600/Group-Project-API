from utils.auth_utils import verifyPassword, generateAuthToken
from schema.auth_schema import LoginRequest, LoginResponse, UserSchema
from repositories.auth_repo import UserRepository
from sqlalchemy.orm import Session
from fastapi import Response

class AuthService:
    authRepo = UserRepository()

    def login(self, db: Session, loginRequest: LoginRequest, response: Response):
        #check user exists
        user = self.authRepo.get_user_by_username(db, loginRequest.username)
        if user is None:
            return LoginResponse(
                errorMessage="Username or password was incorrect",
                statusCode=401
            )
        #verify password
        if not verifyPassword(loginRequest.password, user.password_hash):
            return LoginResponse(
                errorMessage="Username or password was incorrect",
                statusCode=401
            )
        #set token for sessions
        token = generateAuthToken()
        response.set_cookie(
            key="session_token",
            value=token,
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=60 * 60
        )

        return LoginResponse(
            user=UserSchema.model_validate(user),
            statusCode=200
        )