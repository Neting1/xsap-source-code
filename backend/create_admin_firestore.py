from firebase_admin import auth
from app.core.firebase import db

user = auth.get_user_by_email(
    "admin@xeonsys.com"
)

db.collection("users").document(
    user.uid
).set(
    {
        "uid": user.uid,
        "email": "admin@xeonsys.com",
        "full_name": "XSAP Administrator",
        "role": "admin",
        "status": "active"
    }
)

print("Admin Firestore document created.")