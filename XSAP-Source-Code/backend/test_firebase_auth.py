from firebase_admin import auth
from app.core.firebase import db

print("Firebase initialized")

page = auth.list_users()

print("Authentication connected")
print(page)