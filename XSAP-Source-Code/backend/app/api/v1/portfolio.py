from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.portfolio import (
    PortfolioCreate,
    PortfolioUpdate
)

from app.services.portfolio_service import (
    add_portfolio,
    fetch_all_portfolios,
    fetch_portfolio,
    edit_portfolio,
    remove_portfolio
)

router = APIRouter(
    prefix="/api/v1/portfolios",
    tags=["Portfolios"]
)


@router.post("/")
def create_portfolio(
    portfolio: PortfolioCreate
):

    return add_portfolio(
        portfolio.investor_id,
        portfolio.portfolio_name,
        portfolio.description
    )


@router.get("/")
def get_all_portfolios():

    portfolios = fetch_all_portfolios()

    return {
        "total_portfolios":
        len(portfolios),
        "portfolios":
        portfolios
    }


@router.get("/{portfolio_id}")
def get_portfolio(
    portfolio_id: str
):

    portfolio = fetch_portfolio(
        portfolio_id
    )

    if not portfolio:

        raise HTTPException(
            status_code=404,
            detail="Portfolio not found"
        )

    return portfolio


@router.put("/{portfolio_id}")
def update_portfolio(
    portfolio_id: str,
    portfolio: PortfolioUpdate
):

    existing = fetch_portfolio(
        portfolio_id
    )

    if not existing:

        raise HTTPException(
            status_code=404,
            detail="Portfolio not found"
        )

    data = portfolio.dict(
        exclude_unset=True
    )

    return edit_portfolio(
        portfolio_id,
        data
    )


@router.delete("/{portfolio_id}")
def delete_portfolio(
    portfolio_id: str
):

    existing = fetch_portfolio(
        portfolio_id
    )

    if not existing:

        raise HTTPException(
            status_code=404,
            detail="Portfolio not found"
        )

    return remove_portfolio(
        portfolio_id
    )