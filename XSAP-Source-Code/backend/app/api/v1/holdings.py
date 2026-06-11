from fastapi import APIRouter

from app.repositories.holding_repository import (
    HoldingRepository
)

from app.services.holding_service import (
    HoldingService
)

router = APIRouter(
    prefix="/api/v1/holdings",
    tags=["Holdings"]
)


@router.get("/")
def get_all_holdings():

    return {
        "total_holdings":
        len(
            HoldingRepository.get_all_holdings()
        ),
        "holdings":
        HoldingRepository.get_all_holdings()
    }


@router.get("/{portfolio_id}")
def get_portfolio_holdings(
    portfolio_id: str
):

    return HoldingService.get_live_portfolio_value(
        portfolio_id
    )