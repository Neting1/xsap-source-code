from firebase_admin import auth
from app.services.firebase_auth_service import firebase_sign_in

from app.core.firebase import db
from app.security.jwt import create_access_token


def register_user(
    full_name: str,
    email: str,
    password: str
):

    try:

        user = auth.create_user(
            email=email,
            password=password,
            display_name=full_name
        )

        db.collection("users").document(
            user.uid
        ).set(
            {
                "uid": user.uid,
                "full_name": full_name,
                "email": email,
                "role": "investor",
                "status": "active"
            }
        )

        return user

    except Exception:
        return None


def login_user(
    email: str,
    password: str
):

    firebase_user = firebase_sign_in(
        email,
        password
    )

    if not firebase_user:
        return None

    token = create_access_token(
        {
            "sub": email,
            "uid": firebase_user["localId"]
        }
    )

    return token