from app.core.firebase import db


class HistoricalPriceRepository:

    COLLECTION = "historical_prices"

    @staticmethod
    def get_prices_by_symbol(
        symbol: str
    ):

        docs = (
            db.collection(
                HistoricalPriceRepository.COLLECTION
            )
            .where(
                "symbol",
                "==",
                symbol
            )
            .stream()
        )

        results = []

        for doc in docs:

            results.append(
                doc.to_dict()
            )

        results.sort(
            key=lambda x:
            x.get("date", "")
        )

        return results

    @staticmethod
    def add_price(
        data: dict
    ):

        db.collection(
            HistoricalPriceRepository.COLLECTION
        ).add(data)

        return data