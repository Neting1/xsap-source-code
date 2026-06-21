from app.services.analytics_engine import (
    AnalyticsEngine
)

from app.services.market_intelligence_engine import (
    MarketIntelligenceEngine
)

from app.services.forecasting_engine import (
    ForecastingEngine
)


class RebalancingEngine:

    @staticmethod
    def analyze_portfolio(
        portfolio_id: str
    ):

        risk = (
            AnalyticsEngine
            .get_risk_analysis(
                portfolio_id
            )
        )

        exposure = (
            MarketIntelligenceEngine
            .get_sector_exposure(
                portfolio_id
            )
        )

        best_sector = (
            MarketIntelligenceEngine
            .get_best_sector()
        )

        portfolio_forecast = (
            ForecastingEngine
            .portfolio_forecast(
                portfolio_id
            )
        )

        recommendations = []

        largest_position = (
            risk.get(
                "largest_position_percent",
                0
            )
        )

        diversification = (
            risk.get(
                "diversification_score",
                0
            )
        )

        if largest_position > 50:

            recommendations.append(
                {
                    "action":
                        "REDUCE",

                    "symbol":
                        "Largest Holding",

                    "reason":
                        "Portfolio concentration exceeds safe threshold"
                }
            )

        if diversification < 40:

            recommendations.append(
                {
                    "action":
                        "DIVERSIFY",

                    "sector":
                        best_sector[
                            "best_sector"
                        ],

                    "reason":
                        "Portfolio diversification is low"
                }
            )

        if (
            portfolio_forecast.get(
                "expected_growth_percent",
                0
            ) < 0
        ):

            recommendations.append(
                {
                    "action":
                        "REVIEW",

                    "reason":
                        "Forecast indicates negative portfolio growth"
                }
            )

        exposure_data = (
            exposure.get(
                "sector_exposure",
                {}
            )
        )

        for sector, percent in (
            exposure_data.items()
        ):

            if percent > 70:

                recommendations.append(
                    {
                        "action":
                            "REDUCE_SECTOR",

                        "sector":
                            sector,

                        "reason":
                            f"{sector} exposure exceeds 70%"
                    }
                )

        if not recommendations:

            recommendations.append(
                {
                    "action":
                        "HOLD",

                    "reason":
                        "Portfolio allocation is healthy"
                }
            )

        return {

            "portfolio_id":
                portfolio_id,

            "current_risk":
                risk[
                    "risk_level"
                ],

            "current_diversification":
                diversification,

            "recommended_actions":
                recommendations
        }