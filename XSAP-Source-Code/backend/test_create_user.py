from firebase_admin import auth
from app.core.firebase import db

try:
    user = auth.create_user(
        email="admin@xeonsys.com",
        password="Admin@123",
        display_name="XSAP Administrator"
    )

    print("User created successfully")
    print("UID:", user.uid)

except Exception as e:
    print("Error:", e)