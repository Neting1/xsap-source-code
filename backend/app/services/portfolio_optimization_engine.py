from app.services.analytics_engine import (
    AnalyticsEngine
)

from app.services.investment_strategy_engine import (
    InvestmentStrategyEngine
)

from app.repositories.portfolio_repository import (
    PortfolioRepository
)


class PortfolioOptimizationEngine:

    @staticmethod
    def optimize_portfolio(
        portfolio_id: str
    ):

        portfolio = (
            PortfolioRepository
            .get_portfolio(
                portfolio_id
            )
        )

        if not portfolio:

            return {

                "portfolio_id":
                    portfolio_id,

                "efficiency_score":
                    0,

                "optimization_status":
                    "Portfolio Not Found",

                "current_allocation":
                    {},

                "target_allocation":
                    {},

                "recommended_actions":
                    []
            }

        investor_id = (
            portfolio.get(
                "investor_id"
            )
        )

        strategy = (
            InvestmentStrategyEngine
            .generate_strategy(
                investor_id
            )
        )

        target_allocation = (
            strategy.get(
                "allocation_plan",
                {}
            )
        )

        portfolio_summary = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        holdings = (
            portfolio_summary.get(
                "holdings",
                []
            )
        )

        total_market_value = (
            portfolio_summary.get(
                "total_market_value",
                0
            )
        )

        current_allocation = {}

        for holding in holdings:

            symbol = (
                holding.get(
                    "symbol"
                )
            )

            market_value = (
                holding.get(
                    "market_value",
                    0
                )
            )

            allocation_percent = 0

            if total_market_value > 0:

                allocation_percent = round(
                    (
                        market_value
                        /
                        total_market_value
                    ) * 100,
                    2
                )

            current_allocation[
                symbol
            ] = allocation_percent

        total_deviation = 0

        recommendations = []

        for sector, target_percent in (
            target_allocation.items()
        ):

            current_percent = (
                current_allocation.get(
                    sector,
                    0
                )
            )

            deviation = abs(
                target_percent
                -
                current_percent
            )

            total_deviation += (
                deviation
            )

            if target_percent > current_percent:

                recommendations.append(
                    f"Increase {sector} allocation by {round(target_percent - current_percent, 2)}%"
                )

            elif current_percent > target_percent:

                recommendations.append(
                    f"Reduce {sector} allocation by {round(current_percent - target_percent, 2)}%"
                )

        efficiency_score = max(
            0,
            round(
                100 -
                (
                    total_deviation / 2
                ),
                2
            )
        )

        if efficiency_score >= 80:

            optimization_status = (
                "Optimized"
            )

        elif efficiency_score >= 60:

            optimization_status = (
                "Acceptable"
            )

        else:

            optimization_status = (
                "Needs Rebalancing"
            )

        return {

            "portfolio_id":
                portfolio_id,

            "efficiency_score":
                efficiency_score,

            "optimization_status":
                optimization_status,

            "current_allocation":
                current_allocation,

            "target_allocation":
                target_allocation,

            "recommended_actions":
                recommendations
        }