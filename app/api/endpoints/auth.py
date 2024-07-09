from fastapi import APIRouter, HTTPException

from app.api.utils.auth import *


auth_router = APIRouter(tags=["Authentication"])


@auth_router.get("/users")
def users_get():
    response, error = get_users()
    if error:
        raise HTTPException(status_code=500, detail=error)
    return response
