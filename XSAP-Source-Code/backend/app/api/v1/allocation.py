from fastapi import APIRouter

from app.services.allocation_service import (
    AllocationService
)

from app.schemas.allocation import (
    AllocationResponse
)

router = APIRouter(
    prefix="/allocation",
    tags=["Allocation Analytics"]
)


@router.get(
    "/{portfolio_id}",
    response_model=
    AllocationResponse
)
def get_allocation(
    portfolio_id: str
):

    return (
        AllocationService
        .get_portfolio_allocation(
            portfolio_id
        )
    )