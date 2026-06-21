from fastapi import APIRouter

from app.services.alert_engine import (
    AlertEngine
)

router = APIRouter(
    prefix="/alerts-engine",
    tags=["AI Alerts"]
)


@router.get(
    "/portfolio/{portfolio_id}"
)
def portfolio_alerts(
    portfolio_id: str
):

    return (
        AlertEngine
        .get_portfolio_alerts(
            portfolio_id
        )
    )


@router.get(
    "/investor/{investor_id}"
)
def investor_alerts(
    investor_id: str
):

    return (
        AlertEngine
        .get_investor_alerts(
            investor_id
        )
    )