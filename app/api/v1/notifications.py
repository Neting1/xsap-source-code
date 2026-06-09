from fastapi import APIRouter

from app.schemas.notification import (
    NotificationCreate
)

from app.services.notification_service import (
    NotificationService
)

router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"]
)


@router.post("/")
def create_notification(
    data: NotificationCreate
):

    return (
        NotificationService
        .create_notification(
            data.dict()
        )
    )


@router.get("/{user_id}")
def get_notifications(
    user_id: str
):

    return (
        NotificationService
        .get_notifications(
            user_id
        )
    )


@router.patch(
    "/read/{notification_id}"
)
def mark_as_read(
    notification_id: str
):

    return {
        "success":
        NotificationService
        .mark_as_read(
            notification_id
        )
    }


@router.delete(
    "/{notification_id}"
)
def delete_notification(
    notification_id: str
):

    return {
        "success":
        NotificationService
        .delete_notification(
            notification_id
        )
    }