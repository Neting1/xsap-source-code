from app.core.firebase import db


class HoldingRepository:

    @staticmethod
    def create_holding(data):

        doc_ref = db.collection(
            "holdings"
        ).document()

        data["holding_id"] = doc_ref.id

        doc_ref.set(data)

        return data

    @staticmethod
    def get_holding(
        portfolio_id,
        stock_symbol
    ):

        docs = (
            db.collection(
                "holdings"
            )
            .where(
                "portfolio_id",
                "==",
                portfolio_id
            )
            .where(
                "stock_symbol",
                "==",
                stock_symbol
            )
            .stream()
        )

        for doc in docs:

            holding = doc.to_dict()

            holding["holding_id"] = doc.id

            return holding

        return None

    @staticmethod
    def get_portfolio_holdings(
        portfolio_id
    ):

        docs = (
            db.collection(
                "holdings"
            )
            .where(
                "portfolio_id",
                "==",
                portfolio_id
            )
            .stream()
        )

        holdings = []

        for doc in docs:

            holding = doc.to_dict()

            holding["holding_id"] = doc.id

            holdings.append(
                holding
            )

        return holdings

    @staticmethod
    def update_holding(
        holding_id,
        data
    ):

        db.collection(
            "holdings"
        ).document(
            holding_id
        ).update(data)

        return True

    @staticmethod
    def delete_holding(
        holding_id
    ):

        db.collection(
            "holdings"
        ).document(
            holding_id
        ).delete()

        return {
            "message":
            "Holding deleted successfully"
        }

    @staticmethod
    def get_all_holdings():

        docs = db.collection(
            "holdings"
        ).stream()

        holdings = []

        for doc in docs:

            holding = doc.to_dict()

            holding["holding_id"] = doc.id

            holdings.append(
                holding
            )

        return holdings