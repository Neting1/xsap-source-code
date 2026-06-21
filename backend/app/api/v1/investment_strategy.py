from fastapi import APIRouter

from app.services.investment_strategy_engine import (
    InvestmentStrategyEngine
)

router = APIRouter(
    prefix="/investment-strategy",
    tags=["Investment Strategy"]
)


@router.get(
    "/investor/{investor_id}"
)
def investor_strategy(
    investor_id: str
):

    return (
        InvestmentStrategyEngine
        .generate_strategy(
            investor_id
        )
    )