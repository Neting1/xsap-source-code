from app.core.firebase import db


class WatchlistRepository:

    @staticmethod
    def create_watchlist(data):

        doc_ref = db.collection(
            "watchlists"
        ).document()

        data["watchlist_id"] = doc_ref.id

        doc_ref.set(data)

        return data

    @staticmethod
    def get_investor_watchlist(
        investor_id
    ):

        docs = (
            db.collection(
                "watchlists"
            )
            .where(
                "investor_id",
                "==",
                investor_id
            )
            .stream()
        )

        watchlists = []

        for doc in docs:

            item = doc.to_dict()

            item["watchlist_id"] = doc.id

            watchlists.append(
                item
            )

        return watchlists

    @staticmethod
    def get_watchlist_item(
        investor_id,
        stock_symbol
    ):

        docs = (
            db.collection(
                "watchlists"
            )
            .where(
                "investor_id",
                "==",
                investor_id
            )
            .where(
                "stock_symbol",
                "==",
                stock_symbol
            )
            .stream()
        )

        for doc in docs:

            item = doc.to_dict()

            item["watchlist_id"] = doc.id

            return item

        return None

    @staticmethod
    def delete_watchlist(
        watchlist_id
    ):

        db.collection(
            "watchlists"
        ).document(
            watchlist_id
        ).delete()

        return True