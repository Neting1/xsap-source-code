from app.core.firebase import db


class DashboardRepository:

    @staticmethod
    def get_investor_portfolios(
        investor_id
    ):

        docs = db.collection(
            "portfolios"
        ).where(
            "investor_id",
            "==",
            investor_id
        ).stream()

        return [
            doc.to_dict()
            for doc in docs
        ]

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