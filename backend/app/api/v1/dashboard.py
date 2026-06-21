from fastapi import APIRouter

from app.services.dashboard_service import (
    DashboardService
)

from app.schemas.dashboard import (
    InvestorDashboardResponse
)

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/investor/{investor_id}",
    response_model=InvestorDashboardResponse
)
def investor_dashboard(
    investor_id: str
):

    return (
        DashboardService
        .get_investor_dashboard(
            investor_id
        )
    )