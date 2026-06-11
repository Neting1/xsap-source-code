from fastapi import APIRouter

from app.services.analytics_service import (
    AnalyticsService
)

router = APIRouter(
    prefix="/api/v1/analytics",
    tags=["Analytics"]
)

@router.get(
    "/portfolio/{portfolio_id}"
)
def portfolio_analytics(
    portfolio_id: str
):

    return AnalyticsService.get_portfolio_summary(
        portfolio_id
    )