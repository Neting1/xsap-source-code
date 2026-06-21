from app.core.firebase import db


def get_user_by_uid(uid: str):

    doc = db.collection(
        "users"
    ).document(uid).get()

    if doc.exists:
        return doc.to_dict()

    return None


def get_all_users():

    docs = db.collection(
        "users"
    ).stream()

    users = []

    for doc in docs:
        users.append(doc.to_dict())

    return users