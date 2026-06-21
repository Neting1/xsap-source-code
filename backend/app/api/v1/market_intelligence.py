from fastapi import APIRouter

from app.services.market_intelligence_engine import (
    MarketIntelligenceEngine
)

router = APIRouter(
    prefix="/market-intelligence",
    tags=["Market Intelligence"]
)


@router.get(
    "/sector-performance"
)
def sector_performance():

    return (
        MarketIntelligenceEngine
        .get_sector_performance()
    )


@router.get(
    "/best-sector"
)
def best_sector():

    return (
        MarketIntelligenceEngine
        .get_best_sector()
    )


@router.get(
    "/sector-exposure/{portfolio_id}"
)
def sector_exposure(
    portfolio_id: str
):

    return (
        MarketIntelligenceEngine
        .get_sector_exposure(
            portfolio_id
        )
    )


@router.get(
    "/rotation-opportunities"
)
def rotation_opportunities():

    return (
        MarketIntelligenceEngine
        .get_rotation_opportunities()
    )