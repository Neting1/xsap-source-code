from fastapi import APIRouter

from app.services.watchlist_analytics_service import (
    WatchlistAnalyticsService
)

from app.services.watchlist_ai_service import (
    WatchlistAIService
)

router = APIRouter(
    prefix="/api/v1/watchlist-analytics",
    tags=["Watchlist Analytics"]
)


@router.get(
    "/{investor_id}"
)
def analytics(
    investor_id: str
):

    return (
        WatchlistAnalyticsService
        .get_watchlist_analytics(
            investor_id
        )
    )


@router.get(
    "/opportunities/{investor_id}"
)
def opportunities(
    investor_id: str
):

    return (
        WatchlistAIService
        .get_opportunities(
            investor_id
        )
    )