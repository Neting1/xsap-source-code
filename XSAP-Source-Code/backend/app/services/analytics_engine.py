from app.repositories.holding_repository import (
    get_holdings_by_user
)

from app.services.providers.gse_provider import (
    GSEProvider
)

provider = GSEProvider()


def calculate_portfolio(user_id):

    holdings = get_holdings_by_user(user_id)

    total_market_value = 0
    total_cost_basis = 0

    holding_results = []

    for holding in holdings:

        symbol = holding["symbol"]
        quantity = holding["quantity"]
        purchase_price = holding["purchase_price"]

        market_data = provider.get_stock(symbol)

        current_price = market_data.get(
            "price",
            purchase_price
        )

        market_value = (
            quantity * current_price
        )

        cost_basis = (
            quantity * purchase_price
        )

        profit_loss = (
            market_value - cost_basis
        )

        profit_percent = 0

        if cost_basis > 0:

            profit_percent = round(
                (profit_loss / cost_basis)
                * 100,
                2
            )

        total_market_value += market_value
        total_cost_basis += cost_basis

        holding_results.append({
            "symbol": symbol,
            "quantity": quantity,
            "purchase_price": purchase_price,
            "current_price": current_price,
            "market_value": market_value,
            "cost_basis": cost_basis,
            "profit_loss": profit_loss,
            "profit_percent": profit_percent
        })

    total_profit = (
        total_market_value
        - total_cost_basis
    )

    total_return_percent = 0

    if total_cost_basis > 0:

        total_return_percent = round(
            (
                total_profit
                / total_cost_basis
            ) * 100,
            2
        )

    return {
        "total_market_value":
        total_market_value,

        "total_cost_basis":
        total_cost_basis,

        "total_profit":
        total_profit,

        "total_return_percent":
        total_return_percent,

        "holdings":
        holding_results
    }