from fastapi import APIRouter

from app.services.intelligence_engine import (
    IntelligenceEngine
)

from app.schemas.intelligence import (
    IntelligenceResponse
)

router = APIRouter(
    prefix="/api/v1/intelligence",
    tags=["Portfolio Intelligence"]
)


@router.get(
    "/{portfolio_id}",
    response_model=
    IntelligenceResponse
)
def get_intelligence(
    portfolio_id: str
):

    return (
        IntelligenceEngine
        .get_portfolio_intelligence(
            portfolio_id
        )
    )