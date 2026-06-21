from fastapi import APIRouter

from app.services.risk_profile_engine import (
    RiskProfileEngine
)

router = APIRouter(
    prefix="/risk-profile",
    tags=["Risk Profile"]
)


@router.get(
    "/investor/{investor_id}"
)
def investor_profile(
    investor_id: str
):

    return (
        RiskProfileEngine
        .assess_investor(
            investor_id
        )
    )


@router.get(
    "/compatibility/{investor_id}/{portfolio_id}"
)
def portfolio_compatibility(
    investor_id: str,
    portfolio_id: str
):

    return (
        RiskProfileEngine
        .check_portfolio_compatibility(
            investor_id,
            portfolio_id
        )
    )