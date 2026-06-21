from fastapi import APIRouter

from app.services.admin_service import (
    AdminService
)

from app.schemas.admin import (
    SystemStatisticsResponse
)

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


@router.get(
    "/statistics",
    response_model=
    SystemStatisticsResponse
)
def system_statistics():

    return (
        AdminService
        .get_system_statistics()
    )


@router.get(
    "/investors"
)
def get_investors():

    return (
        AdminService
        .get_all_investors()
    )


@router.put(
    "/investors/{uid}/suspend"
)
def suspend_investor(
    uid: str
):

    return (
        AdminService
        .suspend_investor(
            uid
        )
    )


@router.put(
    "/investors/{uid}/activate"
)
def activate_investor(
    uid: str
):

    return (
        AdminService
        .activate_investor(
            uid
        )
    )


@router.get(
    "/analytics/most-traded"
)
def most_traded_stocks():

    return (
        AdminService
        .get_most_traded_stocks()
    )


@router.get(
    "/analytics/active-investors"
)
def active_investors():

    return (
        AdminService
        .get_most_active_investors()
    )


@router.get(
    "/analytics/market-value"
)
def market_value():

    return (
        AdminService
        .get_total_market_value()
    )


@router.get(
    "/analytics/system-health"
)
def system_health():

    return (
        AdminService
        .get_system_health()
    )