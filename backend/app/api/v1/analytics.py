from fastapi import APIRouter
from fastapi import HTTPException

from app.services.analytics_service import (
    AnalyticsService
)

router = APIRouter(
    prefix="/api/v1/analytics",
    tags=["Analytics"]
)


@router.get("/portfolio/{portfolio_id}")
def portfolio_summary(
    portfolio_id: str
):

    return AnalyticsService.get_portfolio_summary(
        portfolio_id
    )


@router.get("/allocation/{portfolio_id}")
def allocation_analysis(
    portfolio_id: str
):

    return AnalyticsService.get_allocation_analysis(
        portfolio_id
    )


@router.get("/top-performers/{portfolio_id}")
def top_performers(
    portfolio_id: str
):

    return AnalyticsService.get_top_performers(
        portfolio_id
    )


@router.get("/risk/{portfolio_id}")
def risk_analysis(
    portfolio_id: str
):

    return AnalyticsService.get_risk_analysis(
        portfolio_id
    )