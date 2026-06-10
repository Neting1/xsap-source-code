from app.repositories.holding_repository import (
    HoldingRepository
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