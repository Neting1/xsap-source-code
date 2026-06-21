from fastapi import APIRouter

from app.services.executive_dashboard_service import (
    ExecutiveDashboardService
)

from app.schemas.executive_dashboard import (
    ExecutiveDashboardResponse
)

router = APIRouter(
    prefix="/api/v1/executive-dashboard",
    tags=["Executive Dashboard"]
)


@router.get(
    "/",
    response_model=
    ExecutiveDashboardResponse
)
def executive_dashboard():

    return (
        ExecutiveDashboardService
        .get_dashboard()
    )