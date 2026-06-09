from datetime import datetime

from app.repositories.notification_repository import (
    NotificationRepository
)


class NotificationService:

    @staticmethod
    def create_notification(data):

        data["read"] = False

        data["created_at"] = (
            datetime.utcnow().isoformat()
        )

        return (
            NotificationRepository
            .create_notification(data)
        )

    @staticmethod
    def get_notifications(user_id):

        return (
            NotificationRepository
            .get_notifications(user_id)
        )

    @staticmethod
    def mark_as_read(notification_id):

        return (
            NotificationRepository
            .mark_as_read(notification_id)
        )

    @staticmethod
    def delete_notification(notification_id):

        return (
            NotificationRepository
            .delete_notification(notification_id)
        )