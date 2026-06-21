from app.core.firebase import db


class AlertRepository:

    @staticmethod
    def create_alert(
        data
    ):

        doc_ref = (
            db.collection(
                "price_alerts"
            ).document()
        )

        data["alert_id"] = (
            doc_ref.id
        )

        doc_ref.set(data)

        return data

    @staticmethod
    def get_user_alerts(
        user_id
    ):

        docs = (
            db.collection(
                "price_alerts"
            )
            .where(
                "user_id",
                "==",
                user_id
            )
            .stream()
        )

        alerts = []

        for doc in docs:

            alert = (
                doc.to_dict()
            )

            alert[
                "alert_id"
            ] = doc.id

            alerts.append(
                alert
            )

        return alerts

    @staticmethod
    def update_alert(
        alert_id,
        data
    ):

        (
            db.collection(
                "price_alerts"
            )
            .document(
                alert_id
            )
            .update(data)
        )

        return True

    @staticmethod
    def delete_alert(
        alert_id
    ):

        (
            db.collection(
                "price_alerts"
            )
            .document(
                alert_id
            )
            .delete()
        )

        return True