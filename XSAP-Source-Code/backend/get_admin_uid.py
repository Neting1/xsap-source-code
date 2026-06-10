from firebase_admin import auth
from app.core.firebase import db

user = auth.get_user_by_email(
    "admin@xeonsys.com"
)

print("UID:", user.uid)