from app.core.firebase import db


class PortfolioRepository:

    @staticmethod
    def create_portfolio(data):

        doc_ref = db.collection(
            "portfolios"
        ).document()

        data["portfolio_id"] = doc_ref.id
        data["total_value"] = 0
        data["status"] = "active"

        doc_ref.set(data)

        return data

    @staticmethod
    def get_all_portfolios():

        docs = db.collection(
            "portfolios"
        ).stream()

        return [
            doc.to_dict()
            for doc in docs
        ]

    @staticmethod
    def get_portfolio(portfolio_id):

        doc = db.collection(
            "portfolios"
        ).document(
            portfolio_id
        ).get()

        if doc.exists:
            return doc.to_dict()

        return None

    @staticmethod
    def update_portfolio(
        portfolio_id,
        data
    ):

        doc_ref = db.collection(
            "portfolios"
        ).document(
            portfolio_id
        )

        doc_ref.update(data)

        return doc_ref.get().to_dict()

    @staticmethod
    def update_portfolio_value(
        portfolio_id,
        new_value
    ):

        db.collection(
            "portfolios"
        ).document(
            portfolio_id
        ).update(
            {
                "total_value": new_value
            }
        )

        return True

    @staticmethod
    def delete_portfolio(
        portfolio_id
    ):

        db.collection(
            "portfolios"
        ).document(
            portfolio_id
        ).delete()

        return {
            "message":
            "Portfolio deleted successfully"
        }