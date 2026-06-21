from fastapi import APIRouter

from app.services.portfolio_optimization_engine import (
    PortfolioOptimizationEngine
)

router = APIRouter(
    prefix="/portfolio-optimization",
    tags=[
        "Portfolio Optimization"
    ]
)


@router.get(
    "/{portfolio_id}"
)
def optimize_portfolio(
    portfolio_id: str
):

    return (
        PortfolioOptimizationEngine
        .optimize_portfolio(
            portfolio_id
        )
    )