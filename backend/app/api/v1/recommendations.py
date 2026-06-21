from fastapi import APIRouter

from app.services.recommendation_engine import (
    RecommendationEngine
)

from app.schemas.recommendation import (
    RecommendationResponse
)

router = APIRouter(
    prefix="/api/v1/recommendations",
    tags=["AI Recommendations"]
)


@router.get(
    "/{portfolio_id}",
    response_model=
    RecommendationResponse
)
def get_recommendations(
    portfolio_id: str
):

    return (
        RecommendationEngine
        .get_recommendations(
            portfolio_id
        )
    )