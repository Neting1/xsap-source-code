from app.core.firebase import db


class AllocationRepository:

    @staticmethod
    def get_holdings_by_portfolio(
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