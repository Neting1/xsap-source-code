from app.core.firebase import db


class TransactionRepository:

    @staticmethod
    def create_transaction(transaction_data):

        transaction_id = db.collection(
            "transactions"
        ).document().id

        transaction_data["transaction_id"] = transaction_id

        db.collection(
            "transactions"
        ).document(transaction_id).set(
            transaction_data
        )

        return transaction_data

    @staticmethod
    def get_transaction(transaction_id):

        doc = db.collection(
            "transactions"
        ).document(transaction_id).get()

        if doc.exists:
            return doc.to_dict()

        return None

    @staticmethod
    def get_all_transactions():

        docs = db.collection(
            "transactions"
        ).stream()

        return [
            doc.to_dict()
            for doc in docs
        ]

    @staticmethod
    def delete_transaction(transaction_id):

        db.collection(
            "transactions"
        ).document(transaction_id).delete()

        return True