from fastapi import APIRouter, HTTPException

from app.api.utils.auth import *
from app.api.schemas.auth import *
from app.core.config import ACCESS_EXPIRY, REFRESH_EXPIRY

from app.core.security import AuthHandler


auth_router = APIRouter(tags=["Authentication"])

auth_handler = AuthHandler()


@auth_router.post("/auth/login", response_model=LoginResponse)
def email_login(user_data: EmailLogin):
    login_response, error = login(user_data)
    if error:
        raise HTTPException(status_code=409, detail=error)
    else:
        access_token, refresh_token = auth_handler.generate_tokens(login_response.get("id"))
        login_response["access_token"] = access_token
        login_response["refresh_token"] = refresh_token
        login_response["access_token_expires_in"] = ACCESS_EXPIRY
    return login_response


@auth_router.post("/auth/register", response_model=LoginResponse)
def email_register(user_data: EmailRegister):
    register_response, error = register(user_data)
    if error:
        raise HTTPException(status_code=409, detail=error)
    else:
        access_token, refresh_token = auth_handler.generate_tokens(register_response.get("id"))
        register_response["access_token"] = access_token
        register_response["refresh_token"] = refresh_token
        register_response["access_token_expires_in"] = ACCESS_EXPIRY
    return register_response


@auth_router.post("/auth/google_login", response_model=LoginResponse)
def google_login(user_data: GoogleLogin):
    login_response, error = login_google(user_data)
    if error:
        raise HTTPException(status_code=409, detail=error)
    else:
        access_token, refresh_token = auth_handler.generate_tokens(login_response.get("id"))
        login_response["access_token"] = access_token
        login_response["refresh_token"] = refresh_token
        login_response["access_token_expires_in"] = ACCESS_EXPIRY
    return login_response


@auth_router.get("/auth/refresh_token", response_model=RefreshResponse)
def refresh_token(refresh_token: str):
    refresh_response, error = token_refresh(refresh_token)
    if error:
        raise HTTPException(status_code=401, detail=error)
    refresh_response["refresh_token_expires_in"] = REFRESH_EXPIRY
    return refresh_response
