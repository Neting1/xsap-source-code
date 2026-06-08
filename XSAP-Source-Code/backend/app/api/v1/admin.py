from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.security.dependencies import (
    get_current_user
)

from app.repositories.user_repository import (
    get_all_users
)

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def admin_dashboard(
    current_user=Depends(get_current_user)
):

    if current_user["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return {
        "message": "Welcome XSAP Administrator",
        "user": current_user
    }


@router.get("/users")
def get_users(
    current_user=Depends(get_current_user)
):

    if current_user["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    users = get_all_users()

    return {
        "total_users": len(users),
        "users": users
    }