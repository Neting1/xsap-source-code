import requests

from app.core.config import settings


def firebase_sign_in(
    email: str,
    password: str
):

    url = (
        "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        f"?key={settings.FIREBASE_API_KEY}"
    )

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(
        url,
        json=payload
    )

    if response.status_code == 200:
        return response.json()

    return None