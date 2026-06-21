from fastapi import APIRouter

from app.services.rebalancing_engine import (
    RebalancingEngine
)

router = APIRouter(
    prefix="/rebalancing",
    tags=["Rebalancing"]
)


@router.get(
    "/portfolio/{portfolio_id}"
)
def rebalance_portfolio(
    portfolio_id: str
):

    return (
        RebalancingEngine
        .analyze_portfolio(
            portfolio_id
        )
    )