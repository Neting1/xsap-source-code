from app.services.providers.gse_provider import (
    GSEProvider
)


class MarketInsightService:

    @staticmethod
    def get_market_overview():

        provider = GSEProvider()

        stocks = provider.get_all_stocks()

        gainers = []

        losers = []

        for stock in stocks:

            try:

                change = float(
                    stock.get(
                        "change_percent",
                        0
                    )
                )

                if change > 0:

                    gainers.append(
                        stock
                    )

                elif change < 0:

                    losers.append(
                        stock
                    )

            except Exception:
                pass

        return {

            "top_gainers":
                sorted(
                    gainers,
                    key=lambda x:
                    float(
                        x.get(
                            "change_percent",
                            0
                        )
                    ),
                    reverse=True
                )[:5],

            "top_losers":
                sorted(
                    losers,
                    key=lambda x:
                    float(
                        x.get(
                            "change_percent",
                            0
                        )
                    )
                )[:5]
        }