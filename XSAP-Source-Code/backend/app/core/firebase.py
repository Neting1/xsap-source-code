import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth

if not firebase_admin._apps:

    cred = credentials.Certificate(
        "firebase/serviceAccountKey.json"
    )

    firebase_admin.initialize_app(cred)

db = firestore.client()

firebase_auth = auth