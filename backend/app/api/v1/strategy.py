from fastapi import APIRouter

from app.services.strategy_engine import (
    StrategyEngine
)

router = APIRouter(
    prefix="/api/v1/strategy",
    tags=["Strategy Simulator"]
)


@router.get(
    "/simulate/{symbol}"
)
def simulate_strategy(
    symbol: str,
    buy_price: float,
    sell_price: float,
    capital: float
):

    return (
        StrategyEngine
        .simulate_strategy(
            symbol,
            buy_price,
            sell_price,
            capital
        )
    )


@router.get(
    "/performance/{symbol}"
)
def strategy_performance(
    symbol: str
):

    return (
        StrategyEngine
        .get_strategy_performance(
            symbol
        )
    )


@router.get(
    "/compare/{symbol}"
)
def compare_strategies(
    symbol: str
):

    return (
        StrategyEngine
        .compare_strategies(
            symbol
        )
    )