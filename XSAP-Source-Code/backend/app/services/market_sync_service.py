from app.core.firebase import db

from app.services.providers.gse_provider import (
    GSEProvider
)

provider = GSEProvider()


def sync_gse_market():

    stocks = provider.get_all_stocks()

    for stock in stocks:

        symbol = stock.get("name")

        if symbol:

            db.collection(
                "stocks"
            ).document(
                symbol
            ).set(stock)

    return {
        "message":
        f"{len(stocks)} stocks synced"
    }