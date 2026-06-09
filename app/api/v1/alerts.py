from fastapi import APIRouter

from app.schemas.alert import (
    AlertCreate
)

from app.services.alert_service import (
    AlertService
)

router = APIRouter(
    prefix="/alerts",
    tags=["Price Alerts"]
)


@router.post("/")
def create_alert(
    data: AlertCreate
):

    return (
        AlertService
        .create_alert(
            data.dict()
        )
    )
    
@router.post("/check")
def check_alerts():

    return (
        AlertService
        .check_alerts()
    )


@router.get("/{user_id}")
def get_alerts(
    user_id: str
):

    return (
        AlertService
        .get_alerts(
            user_id
        )
    )


@router.delete("/{alert_id}")
def delete_alert(
    alert_id: str
):

    return {
        "deleted":
        AlertService
        .delete_alert(
            alert_id
        )
    }