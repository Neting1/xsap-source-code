from app.services.watchlist_analytics_service import (
    WatchlistAnalyticsService
)


class WatchlistAIService:

    @staticmethod
    def get_opportunities(
        investor_id: str
    ):

        analytics = (
            WatchlistAnalyticsService
            .get_watchlist_analytics(
                investor_id
            )
        )

        opportunities = []

        for stock in analytics:

            if stock[
                "change_percent"
            ] < -5:

                opportunities.append(
                    {
                        "symbol":
                            stock["symbol"],

                        "signal":
                            "BUY_OPPORTUNITY",

                        "reason":
                            "Stock has dropped significantly."
                    }
                )

            elif stock[
                "change_percent"
            ] > 8:

                opportunities.append(
                    {
                        "symbol":
                            stock["symbol"],

                        "signal":
                            "MOMENTUM",

                        "reason":
                            "Strong upward trend detected."
                    }
                )

        return opportunities