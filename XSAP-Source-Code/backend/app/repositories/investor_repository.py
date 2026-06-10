from app.core.firebase import db


def create_investor(data: dict):

    doc_ref = db.collection(
        "investors"
    ).document()

    data["investor_id"] = doc_ref.id

    doc_ref.set(data)

    return data


def get_all_investors():

    docs = db.collection(
        "investors"
    ).stream()

    investors = []

    for doc in docs:
        investors.append(
            doc.to_dict()
        )

    return investors


def get_investor_by_id(
    investor_id: str
):

    doc = db.collection(
        "investors"
    ).document(
        investor_id
    ).get()

    if doc.exists:
        return doc.to_dict()

    return None


def update_investor(
    investor_id: str,
    data: dict
):

    doc_ref = db.collection(
        "investors"
    ).document(
        investor_id
    )

    doc = doc_ref.get()

    if not doc.exists:
        return None

    doc_ref.update(data)

    return doc_ref.get().to_dict()


def delete_investor(
    investor_id: str
):

    doc_ref = db.collection(
        "investors"
    ).document(
        investor_id
    )

    doc = doc_ref.get()

    if not doc.exists:
        return False

    doc_ref.delete()

    return True