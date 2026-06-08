from app.repositories.dashboard_repository import (
    DashboardRepository
)


class DashboardService:

    @staticmethod
    def get_investor_dashboard(
        investor_id
    ):

        portfolios = (
            DashboardRepository
            .get_investor_portfolios(
                investor_id
            )
        )

        total_portfolios = len(
            portfolios
        )

        total_holdings = 0
        total_investment = 0
        current_market_value = 0

        for portfolio in portfolios:

            holdings = (
                DashboardRepository
                .get_portfolio_holdings(
                    portfolio[
                        "portfolio_id"
                    ]
                )
            )

            total_holdings += len(
                holdings
            )

            for holding in holdings:

                market_value = holding.get(
                    "market_value",
                    0
                )

                total_investment += (
                    market_value
                )

                current_market_value += (
                    market_value
                )

        profit_loss = (
            current_market_value -
            total_investment
        )

        roi_percentage = 0

        if total_investment > 0:

            roi_percentage = round(
                (
                    profit_loss /
                    total_investment
                ) * 100,
                2
            )

        return {
            "investor_id":
                investor_id,
            "total_portfolios":
                total_portfolios,
            "total_holdings":
                total_holdings,
            "total_investment":
                total_investment,
            "current_market_value":
                current_market_value,
            "profit_loss":
                profit_loss,
            "roi_percentage":
                roi_percentage
        }