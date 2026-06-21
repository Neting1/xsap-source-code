from app.repositories.portfolio_repository import (
    PortfolioRepository
)


def add_portfolio(
    investor_id,
    portfolio_name,
    description
):

    portfolio = {
        "investor_id": investor_id,
        "portfolio_name": portfolio_name,
        "description": description
    }

    return PortfolioRepository.create_portfolio(
        portfolio
    )


def fetch_all_portfolios():

    return PortfolioRepository.get_all_portfolios()


def fetch_portfolio(
    portfolio_id
):

    return PortfolioRepository.get_portfolio(
        portfolio_id
    )


def edit_portfolio(
    portfolio_id,
    data
):

    return PortfolioRepository.update_portfolio(
        portfolio_id,
        data
    )


def remove_portfolio(
    portfolio_id
):

    return PortfolioRepository.delete_portfolio(
        portfolio_id
    )