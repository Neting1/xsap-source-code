from app.repositories.holding_repository import (
    HoldingRepository
)

from app.services.providers.gse_provider import (
    GSEProvider
)


class AnalyticsEngine:

    @staticmethod
    def get_portfolio_summary(
        portfolio_id: str
    ):

        provider = GSEProvider()

        holdings = (
            HoldingRepository
            .get_portfolio_holdings(
                portfolio_id
            )
        )

        total_market_value = 0
        total_cost_basis = 0

        holding_results = []

        for holding in holdings:

            symbol = holding.get(
                "stock_symbol"
            )

            quantity = holding.get(
                "quantity",
                0
            )

            average_price = holding.get(
                "average_price",
                0
            )

            market_data = (
                provider.get_stock(
                    symbol
                )
            )

            current_price = average_price

            if market_data:

                try:

                    current_price = float(
                        market_data.get(
                            "price",
                            average_price
                        )
                    )

                except (
                    ValueError,
                    TypeError
                ):

                    current_price = average_price

            market_value = (
                quantity *
                current_price
            )

            cost_basis = (
                quantity *
                average_price
            )

            profit_loss = (
                market_value -
                cost_basis
            )

            roi_percent = 0

            if cost_basis > 0:

                roi_percent = round(
                    (
                        profit_loss /
                        cost_basis
                    ) * 100,
                    2
                )

            total_market_value += (
                market_value
            )

            total_cost_basis += (
                cost_basis
            )

            holding_results.append(
                {
                    "symbol":
                        symbol,

                    "quantity":
                        quantity,

                    "average_price":
                        round(
                            average_price,
                            2
                        ),

                    "current_price":
                        round(
                            current_price,
                            2
                        ),

                    "cost_basis":
                        round(
                            cost_basis,
                            2
                        ),

                    "market_value":
                        round(
                            market_value,
                            2
                        ),

                    "profit_loss":
                        round(
                            profit_loss,
                            2
                        ),

                    "roi_percent":
                        roi_percent
                }
            )

        total_profit_loss = (
            total_market_value -
            total_cost_basis
        )

        portfolio_roi = 0

        if total_cost_basis > 0:

            portfolio_roi = round(
                (
                    total_profit_loss /
                    total_cost_basis
                ) * 100,
                2
            )

        holdings_count = len(
            holding_results
        )

        return {

            "portfolio_id":
                portfolio_id,

            "holdings_count":
                holdings_count,

            "total_cost_basis":
                round(
                    total_cost_basis,
                    2
                ),

            "total_market_value":
                round(
                    total_market_value,
                    2
                ),

            "total_profit_loss":
                round(
                    total_profit_loss,
                    2
                ),

            "portfolio_roi_percent":
                portfolio_roi,

            "holdings":
                holding_results
        }

    @staticmethod
    def get_risk_analysis(
        portfolio_id: str
    ):

        summary = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        holdings = summary[
            "holdings"
        ]

        if not holdings:

            return {

                "risk_level":
                    "Low",

                "holdings_count":
                    0,

                "largest_position_percent":
                    0,

                "diversification_score":
                    0
            }

        total_value = summary[
            "total_market_value"
        ]

        largest_position = max(
            holdings,
            key=lambda h:
            h["market_value"]
        )

        largest_percent = 0

        if total_value > 0:

            largest_percent = round(
                (
                    largest_position[
                        "market_value"
                    ]
                    /
                    total_value
                ) * 100,
                2
            )

        diversification_score = round(
            100 -
            largest_percent,
            2
        )

        risk_level = "Low"

        if largest_percent > 50:

            risk_level = "High"

        elif largest_percent > 30:

            risk_level = "Medium"

        return {

            "risk_level":
                risk_level,

            "holdings_count":
                len(
                    holdings
                ),

            "largest_position_percent":
                largest_percent,

            "diversification_score":
                diversification_score
        }

    @staticmethod
    def get_top_performers(
        portfolio_id: str
    ):

        summary = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        holdings = summary[
            "holdings"
        ]

        holdings.sort(
            key=lambda h:
            h["roi_percent"],
            reverse=True
        )

        return holdings[:5]

    @staticmethod
    def get_top_losers(
        portfolio_id: str
    ):

        summary = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        holdings = summary[
            "holdings"
        ]

        holdings.sort(
            key=lambda h:
            h["roi_percent"]
        )

        return holdings[:5]