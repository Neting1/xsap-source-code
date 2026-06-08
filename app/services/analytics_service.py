from app.repositories.analytics_repository import (
    AnalyticsRepository
)


class AnalyticsService:

    @staticmethod
    def get_portfolio_summary(
        portfolio_id
    ):

        portfolio = AnalyticsRepository.get_portfolio(
            portfolio_id
        )

        if not portfolio:
            return None

        holdings = (
            AnalyticsRepository.get_portfolio_holdings(
                portfolio_id
            )
        )

        total_investment = 0
        current_market_value = 0

        for holding in holdings:

            invested = (
                holding["quantity"]
                * holding["average_price"]
            )

            market_value = (
                holding["market_value"]
            )

            total_investment += invested
            current_market_value += market_value

        profit_loss = (
            current_market_value
            - total_investment
        )

        roi = 0

        if total_investment > 0:

            roi = (
                profit_loss
                / total_investment
            ) * 100

        return {
            "portfolio_id": portfolio_id,
            "portfolio_name":
                portfolio["portfolio_name"],
            "total_investment":
                round(total_investment, 2),
            "current_market_value":
                round(current_market_value, 2),
            "profit_loss":
                round(profit_loss, 2),
            "roi_percentage":
                round(roi, 2)
        }