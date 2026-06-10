from app.core.firebase import db


class AnalyticsRepository:

    @staticmethod
    def get_portfolio_holdings(
        portfolio_id
    ):

        docs = db.collection(
            "holdings"
        ).where(
            "portfolio_id",
            "==",
            portfolio_id
        ).stream()

        return [
            doc.to_dict()
            for doc in docs
        ]

    @staticmethod
    def get_portfolio(
        portfolio_id
    ):

        doc = db.collection(
            "portfolios"
        ).document(
            portfolio_id
        ).get()

        if doc.exists:
            return doc.to_dict()

        return None