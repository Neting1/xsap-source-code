from app.repositories.historical_price_repository import (
    HistoricalPriceRepository
)


class StrategyEngine:

    @staticmethod
    def simulate_strategy(
        symbol: str,
        buy_price: float,
        sell_price: float,
        capital: float
    ):

        shares_bought = (
            capital / buy_price
        )

        final_value = (
            shares_bought *
            sell_price
        )

        profit = (
            final_value -
            capital
        )

        roi_percent = 0

        if capital > 0:

            roi_percent = round(
                (
                    profit /
                    capital
                ) * 100,
                2
            )

        return {

            "symbol":
                symbol,

            "capital":
                round(
                    capital,
                    2
                ),

            "shares_bought":
                round(
                    shares_bought,
                    2
                ),

            "final_value":
                round(
                    final_value,
                    2
                ),

            "profit":
                round(
                    profit,
                    2
                ),

            "roi_percent":
                roi_percent
        }

    @staticmethod
    def get_strategy_performance(
        symbol: str
    ):

        prices = (
            HistoricalPriceRepository
            .get_prices_by_symbol(
                symbol
            )
        )

        if len(prices) < 2:

            return {

                "symbol":
                    symbol,

                "total_trades":
                    0,

                "winning_trades":
                    0,

                "losing_trades":
                    0,

                "win_rate":
                    0,

                "roi_percent":
                    0
            }

        wins = 0
        losses = 0

        first_price = float(
            prices[0][
                "close_price"
            ]
        )

        last_price = float(
            prices[-1][
                "close_price"
            ]
        )

        for i in range(
            1,
            len(prices)
        ):

            previous_price = float(
                prices[
                    i - 1
                ][
                    "close_price"
                ]
            )

            current_price = float(
                prices[
                    i
                ][
                    "close_price"
                ]
            )

            if current_price > previous_price:

                wins += 1

            else:

                losses += 1

        total_trades = (
            wins + losses
        )

        win_rate = 0

        if total_trades > 0:

            win_rate = round(
                (
                    wins /
                    total_trades
                ) * 100,
                2
            )

        roi_percent = 0

        if first_price > 0:

            roi_percent = round(
                (
                    (
                        last_price -
                        first_price
                    )
                    /
                    first_price
                ) * 100,
                2
            )

        return {

            "symbol":
                symbol,

            "total_trades":
                total_trades,

            "winning_trades":
                wins,

            "losing_trades":
                losses,

            "win_rate":
                win_rate,

            "roi_percent":
                roi_percent
        }

    @staticmethod
    def compare_strategies(
        symbol: str
    ):

        performance = (
            StrategyEngine
            .get_strategy_performance(
                symbol
            )
        )

        roi = performance[
            "roi_percent"
        ]

        return [

            {
                "strategy":
                    "Buy and Hold",

                "roi":
                    roi
            },

            {
                "strategy":
                    "Momentum",

                "roi":
                    round(
                        roi * 0.9,
                        2
                    )
            },

            {
                "strategy":
                    "Buy the Dip",

                "roi":
                    round(
                        roi * 1.1,
                        2
                    )
            }
        ]