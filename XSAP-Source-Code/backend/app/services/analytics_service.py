from app.repositories.analytics_repository import AnalyticsRepository
from app.services.holding_service import HoldingService


class AnalyticsService:

    @staticmethod
    def get_portfolio_summary(portfolio_id):

        return HoldingService.get_live_portfolio_value(
            portfolio_id
        )

    @staticmethod
    def get_allocation_analysis(portfolio_id):

        portfolio = (
            HoldingService.get_live_portfolio_value(
                portfolio_id
            )
        )

        total_value = portfolio["total_market_value"]

        allocations = []

        if total_value <= 0:
            return []

        for holding in portfolio["holdings"]:

            allocation = (
                holding["market_value"]
                / total_value
            ) * 100

            allocations.append(
                {
                    "symbol":
                        holding["symbol"],

                    "market_value":
                        holding["market_value"],

                    "allocation_percent":
                        round(
                            allocation,
                            2
                        )
                }
            )

        return sorted(
            allocations,
            key=lambda x:
            x["allocation_percent"],
            reverse=True
        )

    @staticmethod
    def get_top_performers(portfolio_id):

        portfolio = (
            HoldingService.get_live_portfolio_value(
                portfolio_id
            )
        )

        holdings = sorted(
            portfolio["holdings"],
            key=lambda x:
            x["roi_percent"],
            reverse=True
        )

        return holdings

    @staticmethod
    def get_risk_analysis(portfolio_id):

        portfolio = (
            HoldingService.get_live_portfolio_value(
                portfolio_id
            )
        )

        holdings = portfolio["holdings"]

        total_value = (
            portfolio["total_market_value"]
        )

        if total_value <= 0:

            return {
                "risk_level":
                    "Unknown",

                "diversification_score":
                    0
            }

        largest_position = 0

        for holding in holdings:

            weight = (
                holding["market_value"]
                / total_value
            ) * 100

            if weight > largest_position:
                largest_position = weight

        diversification_score = (
            100 - largest_position
        )

        if largest_position > 60:

            risk_level = "High"

        elif largest_position > 35:

            risk_level = "Medium"

        else:

            risk_level = "Low"

        return {

            "risk_level":
                risk_level,

            "holdings_count":
                len(holdings),

            "largest_position_percent":
                round(
                    largest_position,
                    2
                ),

            "diversification_score":
                round(
                    diversification_score,
                    2
                )
        }