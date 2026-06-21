from app.core.firebase import db


def create_stock(data: dict):

    symbol = data["symbol"]

    db.collection(
        "stocks"
    ).document(
        symbol
    ).set(data)

    return data


def get_all_stocks():

    docs = db.collection(
        "stocks"
    ).stream()

    stocks = []

    for doc in docs:
        stocks.append(
            doc.to_dict()
        )

    return stocks


def get_stock(symbol: str):

    doc = db.collection(
        "stocks"
    ).document(
        symbol
    ).get()

    if doc.exists:
        return doc.to_dict()

    return None


def update_stock(
    symbol: str,
    data: dict
):

    db.collection(
        "stocks"
    ).document(
        symbol
    ).update(data)

    return get_stock(symbol)


def delete_stock(
    symbol: str
):

    db.collection(
        "stocks"
    ).document(
        symbol
    ).delete()

    return {
        "message":
        "Stock deleted successfully"
    }