from fastapi import APIRouter
from fastapi import HTTPException

from app.services.report_service import (
    ReportService
)

router = APIRouter(
    prefix="/api/v1/reports",
    tags=["Reports"]
)


@router.get(
    "/portfolio/{portfolio_id}"
)
def portfolio_report(
    portfolio_id: str
):

    report = (
        ReportService
        .generate_portfolio_report(
            portfolio_id
        )
    )

    if not report:

        raise HTTPException(
            status_code=404,
            detail="Portfolio report not found"
        )

    return report


@router.get(
    "/investor/{investor_id}"
)
def investor_statement(
    investor_id: str
):

    report = (
        ReportService
        .generate_investor_statement(
            investor_id
        )
    )

    if not report:

        raise HTTPException(
            status_code=404,
            detail="Investor report not found"
        )

    return report


@router.get(
    "/portfolio/{portfolio_id}/pdf"
)
def portfolio_pdf_report(
    portfolio_id: str
):

    return (
        ReportService
        .generate_portfolio_pdf(
            portfolio_id
        )
    )


@router.get(
    "/portfolio/{portfolio_id}/excel"
)
def portfolio_excel_report(
    portfolio_id: str
):

    return (
        ReportService
        .generate_portfolio_excel(
            portfolio_id
        )
    )