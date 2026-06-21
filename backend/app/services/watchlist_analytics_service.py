from app.repositories.watchlist_repository import (
    WatchlistRepository
)

from app.services.providers.gse_provider import (
    GSEProvider
)


class WatchlistAnalyticsService:

    @staticmethod
    def get_watchlist_analytics(
        investor_id: str
    ):

        provider = GSEProvider()

        watchlist = (
            WatchlistRepository
            .get_investor_watchlist(
                investor_id
            )
        )

        results = []

        for item in watchlist:

            symbol = item["stock_symbol"]

            stock = (
                provider.get_stock(
                    symbol
                )
            )

            if not stock:
                continue

            try:

                current_price = float(
                    stock.get(
                        "price",
                        0
                    )
                )

                previous_close = float(
                    stock.get(
                        "previous_close",
                        current_price
                    )
                )

            except (
                ValueError,
                TypeError
            ):

                continue

            change = (
                current_price -
                previous_close
            )

            change_percent = 0

            if previous_close > 0:

                change_percent = round(
                    (
                        change /
                        previous_close
                    ) * 100,
                    2
                )

            results.append(
                {
                    "symbol":
                        symbol,

                    "current_price":
                        current_price,

                    "previous_close":
                        previous_close,

                    "change":
                        round(
                            change,
                            2
                        ),

                    "change_percent":
                        change_percent
                }
            )

        return results