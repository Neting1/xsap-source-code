from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends

from app.repositories.user_repository import (
    get_user_by_uid
)

from app.security.dependencies import (
    get_current_user
)

from app.schemas.user import (
    UserRegister,
    UserLogin,
    TokenResponse
)

from app.services.auth_service import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserRegister):

    new_user = register_user(
        user.full_name,
        user.email,
        user.password
    )

    if not new_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return {
        "message": "User registered successfully"
    }


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(user: UserLogin):

    token = login_user(
        user.email,
        user.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token
    }


@router.get("/me")
def get_profile(
    current_user=Depends(
        get_current_user
    )
):

    user = get_user_by_uid(
        current_user["uid"]
    )

    return user