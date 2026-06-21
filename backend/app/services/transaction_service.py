from app.repositories.transaction_repository import (TransactionRepository)

from app.repositories.portfolio_repository import (PortfolioRepository)

from app.services.holding_service import (HoldingService)


class TransactionService:

    @staticmethod
    def create_transaction(data):

        total_amount = (
            data["quantity"] * data["price"]
        )

        data["total_amount"] = total_amount
        data["status"] = "completed"

        portfolio = PortfolioRepository.get_portfolio(
            data["portfolio_id"]
        )

        if not portfolio:
            return {
                "error": "Portfolio not found"
            }

        current_value = portfolio.get(
            "total_value",
            0
        )

        if data["transaction_type"] == "BUY":

            HoldingService.process_buy(
                data["portfolio_id"],
                data["stock_symbol"],
                data["quantity"],
                data["price"]
            )

            new_value = (
                current_value +
                total_amount
            )

        elif data["transaction_type"] == "SELL":

            success = HoldingService.process_sell(
                data["portfolio_id"],
                data["stock_symbol"],
                data["quantity"],
                data["price"]
            )

            if not success:
                return {
                    "error": "Insufficient shares available for sale"
                }

            new_value = (
                current_value -
                total_amount
            )

        else:

            return {
                "error": "Invalid transaction type"
            }

        PortfolioRepository.update_portfolio_value(
            data["portfolio_id"],
            new_value
        )

        return TransactionRepository.create_transaction(
            data
        )

    @staticmethod
    def get_transaction(transaction_id):

        return TransactionRepository.get_transaction(
            transaction_id
        )

    @staticmethod
    def get_all_transactions():

        return TransactionRepository.get_all_transactions()

    @staticmethod
    def delete_transaction(transaction_id):

        return TransactionRepository.delete_transaction(
            transaction_id
        )