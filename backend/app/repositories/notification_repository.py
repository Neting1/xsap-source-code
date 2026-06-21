from app.core.firebase import db


class NotificationRepository:

    COLLECTION = "notifications"

    @staticmethod
    def create_notification(data):

        doc_ref = (
            db.collection(
                NotificationRepository.COLLECTION
            ).document()
        )

        data["notification_id"] = doc_ref.id

        doc_ref.set(data)

        return data

    @staticmethod
    def get_notifications(user_id):

        docs = (
            db.collection(
                NotificationRepository.COLLECTION
            )
            .where(
                "user_id",
                "==",
                user_id
            )
            .stream()
        )

        notifications = []

        for doc in docs:

            item = doc.to_dict()
            item["notification_id"] = doc.id

            notifications.append(item)

        return notifications

    @staticmethod
    def mark_as_read(notification_id):

        (
            db.collection(
                NotificationRepository.COLLECTION
            )
            .document(notification_id)
            .update(
                {
                    "read": True
                }
            )
        )

        return True

    @staticmethod
    def delete_notification(notification_id):

        (
            db.collection(
                NotificationRepository.COLLECTION
            )
            .document(notification_id)
            .delete()
        )

        return True
    
    @staticmethod
    def get_user_notifications(
        user_id
    ):

        docs = (
            db.collection(
                "notifications"
            )
            .where(
                "user_id",
                "==",
                user_id
            )
            .stream()
        )

        return [
            doc.to_dict()
            for doc in docs
        ]