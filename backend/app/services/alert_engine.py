from app.services.analytics_engine import (
    AnalyticsEngine
)

from app.services.intelligence_engine import (
    IntelligenceEngine
)

from app.services.forecasting_engine import (
    ForecastingEngine
)

from app.repositories.portfolio_repository import (
    PortfolioRepository
)


class AlertEngine:

    @staticmethod
    def get_portfolio_alerts(
        portfolio_id: str
    ):

        alerts = []

        risk = (
            AnalyticsEngine
            .get_risk_analysis(
                portfolio_id
            )
        )

        intelligence = (
            IntelligenceEngine
            .get_portfolio_intelligence(
                portfolio_id
            )
        )

        forecast = (
            ForecastingEngine
            .portfolio_forecast(
                portfolio_id
            )
        )

        if (
            risk.get(
                "largest_position_percent",
                0
            ) > 75
        ):

            alerts.append(
                {
                    "alert_type":
                        "RISK_WARNING",

                    "severity":
                        "HIGH",

                    "message":
                        "Portfolio concentration exceeds 75%"
                }
            )

        if (
            risk.get(
                "diversification_score",
                0
            ) < 30
        ):

            alerts.append(
                {
                    "alert_type":
                        "DIVERSIFICATION",

                    "severity":
                        "MEDIUM",

                    "message":
                        "Diversification score below 30"
                }
            )

        if (
            forecast.get(
                "expected_growth_percent",
                0
            ) > 3
        ):

            alerts.append(
                {
                    "alert_type":
                        "PRICE_TARGET",

                    "severity":
                        "INFO",

                    "message":
                        f"Portfolio expected to grow "
                        f"{forecast['expected_growth_percent']}%"
                }
            )

        recommendations = (
            intelligence.get(
                "recommendations",
                []
            )
        )

        for recommendation in recommendations:

            if (
                "undervalued"
                in recommendation.lower()
            ):

                alerts.append(
                    {
                        "alert_type":
                            "BUY_OPPORTUNITY",

                        "severity":
                            "HIGH",

                        "message":
                            recommendation
                    }
                )

        return {

            "portfolio_id":
                portfolio_id,

            "total_alerts":
                len(alerts),

            "alerts":
                alerts
        }

    @staticmethod
    def get_investor_alerts(
        investor_id: str
    ):

        portfolios = (
            PortfolioRepository
            .get_portfolios_by_investor(
                investor_id
            )
        )

        all_alerts = []

        for portfolio in portfolios:

            portfolio_id = (
                portfolio.get(
                    "portfolio_id"
                )
            )

            portfolio_alerts = (
                AlertEngine
                .get_portfolio_alerts(
                    portfolio_id
                )
            )

            all_alerts.extend(
                portfolio_alerts.get(
                    "alerts",
                    []
                )
            )

        return {

            "investor_id":
                investor_id,

            "total_alerts":
                len(all_alerts),

            "alerts":
                all_alerts
        }