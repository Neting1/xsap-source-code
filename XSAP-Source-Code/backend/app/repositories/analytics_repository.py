from app.core.firebase import db


class AnalyticsRepository:

    @staticmethod
    def get_portfolio(portfolio_id):

        doc = (
            db.collection("portfolios")
            .document(portfolio_id)
            .get()
        )

        if doc.exists:
            return doc.to_dict()

        return None

    @staticmethod
    def get_portfolio_holdings(portfolio_id):

        docs = (
            db.collection("holdings")
            .where(
                "portfolio_id",
                "==",
                portfolio_id
            )
            .stream()
        )

        holdings = []

        for doc in docs:

            data = doc.to_dict()

            data["holding_id"] = doc.id

            holdings.append(data)

        return holdings