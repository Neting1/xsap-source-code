from app.repositories.holding_repository import (
    HoldingRepository
)

from app.services.providers.gse_provider import (
    GSEProvider
)


class HoldingService:

    @staticmethod
    def process_buy(
        portfolio_id,
        stock_symbol,
        quantity,
        price
    ):

        holding = HoldingRepository.get_holding(
            portfolio_id,
            stock_symbol
        )

        if not holding:

            return HoldingRepository.create_holding(
                {
                    "portfolio_id": portfolio_id,
                    "stock_symbol": stock_symbol,
                    "quantity": quantity,
                    "average_price": price,
                    "market_value": quantity * price
                }
            )

        new_quantity = (
            holding["quantity"] + quantity
        )

        new_average = (
            (
                holding["quantity"]
                * holding["average_price"]
            )
            +
            (
                quantity * price
            )
        ) / new_quantity

        HoldingRepository.update_holding(
            holding["holding_id"],
            {
                "quantity": new_quantity,
                "average_price": new_average,
                "market_value":
                    new_quantity * price
            }
        )

        return True

    @staticmethod
    def process_sell(
        portfolio_id,
        stock_symbol,
        quantity,
        price
    ):

        holding = HoldingRepository.get_holding(
            portfolio_id,
            stock_symbol
        )

        if not holding:
            return False

        if holding["quantity"] < quantity:
            return False

        remaining = (
            holding["quantity"] - quantity
        )

        HoldingRepository.update_holding(
            holding["holding_id"],
            {
                "quantity": remaining,
                "market_value":
                    remaining * price
            }
        )

        return True

    @staticmethod
    def get_live_portfolio_value(
        portfolio_id
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

        portfolio_holdings = []

        for holding in holdings:

            symbol = holding[
                "stock_symbol"
            ]

            quantity = holding[
                "quantity"
            ]

            average_price = holding[
                "average_price"
            ]

            stock_data = (
                provider.get_stock(
                    symbol
                )
            )

            current_price = 0

            if stock_data:

                try:

                    current_price = float(
                        stock_data.get(
                            "price",
                            0
                        )
                    )

                except (
                    ValueError,
                    TypeError
                ):

                    current_price = 0

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

            roi = 0

            if cost_basis > 0:

                roi = (
                    (
                        profit_loss
                        / cost_basis
                    )
                    * 100
                )

            total_market_value += (
                market_value
            )

            total_cost_basis += (
                cost_basis
            )

            portfolio_holdings.append(
                {
                    "symbol":
                        symbol,

                    "quantity":
                        quantity,

                    "average_price":
                        average_price,

                    "current_price":
                        current_price,

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
                        round(
                            roi,
                            2
                        )
                }
            )

        total_profit_loss = (
            total_market_value -
            total_cost_basis
        )

        portfolio_roi = 0

        if total_cost_basis > 0:

            portfolio_roi = (
                (
                    total_profit_loss
                    / total_cost_basis
                )
                * 100
            )

        return {

            "portfolio_id":
                portfolio_id,

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
                round(
                    portfolio_roi,
                    2
                ),

            "holdings":
                portfolio_holdings
        }
