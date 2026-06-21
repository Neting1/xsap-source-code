from app.repositories.allocation_repository import (
    AllocationRepository
)


class AllocationService:

    @staticmethod
    def get_portfolio_allocation(
        portfolio_id
    ):

        holdings = (
            AllocationRepository
            .get_holdings_by_portfolio(
                portfolio_id
            )
        )

        total_value = sum(
            h.get(
                "market_value",
                0
            )
            for h in holdings
        )

        allocations = []

        for holding in holdings:

            market_value = holding.get(
                "market_value",
                0
            )

            percentage = 0

            if total_value > 0:

                percentage = round(
                    (
                        market_value /
                        total_value
                    ) * 100,
                    2
                )

            allocations.append(
                {
                    "symbol":
                    holding.get(
                        "stock_symbol"
                    ),
                    "market_value":
                    market_value,
                    "allocation_percentage":
                    percentage
                }
            )

        return {
            "portfolio_id":
            portfolio_id,
            "allocations":
            allocations
        }