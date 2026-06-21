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

        portfolios = []

        for doc in docs:

            portfolio = doc.to_dict()

            portfolio["portfolio_id"] = doc.id

            portfolios.append(
                portfolio
            )

        return portfolios

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

            portfolio = doc.to_dict()

            portfolio[
                "portfolio_id"
            ] = doc.id

            return portfolio

        return None

    @staticmethod
    def get_portfolios_by_investor(
        investor_id
    ):

        docs = (
            db.collection(
                "portfolios"
            )
            .where(
                "investor_id",
                "==",
                investor_id
            )
            .stream()
        )

        portfolios = []

        for doc in docs:

            portfolio = doc.to_dict()

            portfolio[
                "portfolio_id"
            ] = doc.id

            portfolios.append(
                portfolio
            )

        return portfolios

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

        updated_doc = (
            doc_ref.get()
        )

        if updated_doc.exists:

            portfolio = (
                updated_doc.to_dict()
            )

            portfolio[
                "portfolio_id"
            ] = updated_doc.id

            return portfolio

        return None

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
                "total_value":
                    new_value
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