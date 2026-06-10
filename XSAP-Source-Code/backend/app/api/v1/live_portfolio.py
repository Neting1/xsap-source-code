from fastapi import APIRouter

from app.services.holding_service import (
    HoldingService
)

router = APIRouter(
    prefix="/live-portfolio",
    tags=["Live Portfolio"]
)


@router.get(
    "/{portfolio_id}"
)
def get_live_portfolio(
    portfolio_id: str
):

    return (
        HoldingService
        .get_live_portfolio_value(
            portfolio_id
        )
    )