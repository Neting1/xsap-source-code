from app.repositories.stock_repository import (
    create_stock,
    get_all_stocks,
    get_stock,
    update_stock,
    delete_stock
)


def add_stock(data):

    data["status"] = "active"

    return create_stock(
        data
    )


def fetch_all_stocks():

    return get_all_stocks()


def fetch_stock(symbol):

    return get_stock(symbol)


def edit_stock(
    symbol,
    data
):

    return update_stock(
        symbol,
        data
    )


def remove_stock(symbol):

    return delete_stock(
        symbol
    )