from pydantic import BaseModel


class EmailLogin(BaseModel):
    email: str
    password: str


class EmailRegister(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class GoogleLogin(BaseModel):
    google_id: str
    email: str
    first_name: str
    last_name: str


class LoginResponse(BaseModel):
    email: str
    first_name: str
    last_name: str
    access_token: str
    refresh_token: str
    access_token_expires_in: int


class RefreshResponse(BaseModel):
    email: str
    access_token: str
    refresh_token_expires_in: int