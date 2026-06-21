from fastapi import APIRouter

from app.services.ai_advisor_service import (
    AIAdvisorService
)

from app.services.market_insight_service import (
    MarketInsightService
)

from app.services.portfolio_scoring_service import (
    PortfolioScoringService
)

router = APIRouter(
    prefix="/api/v1/advisor",
    tags=["AI Advisor"]
)


@router.get(
    "/score/{portfolio_id}"
)
def portfolio_score(
    portfolio_id: str
):

    return (
        PortfolioScoringService
        .calculate_score(
            portfolio_id
        )
    )


@router.get(
    "/recommendations/{portfolio_id}"
)
def recommendations(
    portfolio_id: str
):

    return (
        AIAdvisorService
        .get_advice(
            portfolio_id
        )
    )


@router.get(
    "/market-overview"
)
def market_overview():

    return (
        MarketInsightService
        .get_market_overview()
    )