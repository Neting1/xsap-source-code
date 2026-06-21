from app.services.analytics_engine import (
    AnalyticsEngine
)

from app.services.forecasting_engine import (
    ForecastingEngine
)

from app.repositories.portfolio_repository import (
    PortfolioRepository
)

from app.repositories.holding_repository import (
    HoldingRepository
)


class MarketIntelligenceEngine:

    SECTOR_MAPPING = {

        "MTNGH": "Telecom",
        "GCB": "Banking",
        "CAL": "Banking",
        "ACCESS": "Banking",
        "SCB": "Banking",
        "SIC": "Insurance",
        "EGL": "Insurance",
        "TOTAL": "Energy",
        "GOIL": "Energy",
        "BOPP": "Manufacturing"
    }

    @staticmethod
    def get_sector_performance():

        sectors = {}

        for symbol, sector in (
            MarketIntelligenceEngine
            .SECTOR_MAPPING.items()
        ):

            forecast = (
                ForecastingEngine
                .stock_forecast(
                    symbol
                )
            )

            expected_return = (
                forecast.get(
                    "expected_return",
                    0
                )
            )

            if sector not in sectors:

                sectors[
                    sector
                ] = []

            sectors[
                sector
            ].append(
                expected_return
            )

        results = []

        for sector, returns in (
            sectors.items()
        ):

            avg_return = round(
                sum(returns)
                / len(returns),
                2
            )

            trend = (
                "Bullish"
                if avg_return > 0
                else "Bearish"
            )

            results.append(
                {
                    "sector":
                        sector,

                    "average_return":
                        avg_return,

                    "trend":
                        trend
                }
            )

        return results

    @staticmethod
    def get_best_sector():

        performance = (
            MarketIntelligenceEngine
            .get_sector_performance()
        )

        if not performance:

            return {
                "best_sector":
                    "Unknown",

                "expected_growth":
                    0
            }

        best = max(
            performance,
            key=lambda x:
            x["average_return"]
        )

        return {

            "best_sector":
                best["sector"],

            "expected_growth":
                best[
                    "average_return"
                ]
        }

    @staticmethod
    def get_sector_exposure(
        portfolio_id: str
    ):

        holdings = (
            HoldingRepository
            .get_portfolio_holdings(
                portfolio_id
            )
        )

        analytics = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        total_value = (
            analytics[
                "total_market_value"
            ]
        )

        exposure = {}

        for holding in holdings:

            symbol = (
                holding[
                    "stock_symbol"
                ]
            )

            sector = (
                MarketIntelligenceEngine
                .SECTOR_MAPPING
                .get(
                    symbol,
                    "Other"
                )
            )

            market_value = (
                holding[
                    "quantity"
                ]
                *
                holding[
                    "average_price"
                ]
            )

            exposure[
                sector
            ] = (
                exposure.get(
                    sector,
                    0
                )
                +
                market_value
            )

        for sector in exposure:

            exposure[
                sector
            ] = round(
                (
                    exposure[
                        sector
                    ]
                    /
                    total_value
                ) * 100,
                2
            )

        return {

            "portfolio_id":
                portfolio_id,

            "sector_exposure":
                exposure
        }

    @staticmethod
    def get_rotation_opportunities():

        performance = (
            MarketIntelligenceEngine
            .get_sector_performance()
        )

        if len(
            performance
        ) < 2:

            return []

        sorted_data = sorted(
            performance,
            key=lambda x:
            x[
                "average_return"
            ]
        )

        weakest = (
            sorted_data[0]
        )

        strongest = (
            sorted_data[-1]
        )

        return [

            {
                "from_sector":
                    weakest[
                        "sector"
                    ],

                "to_sector":
                    strongest[
                        "sector"
                    ],

                "reason":
                    "Higher expected sector growth"
            }
        ]