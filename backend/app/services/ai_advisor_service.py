from app.services.analytics_engine import (
    AnalyticsEngine
)


class AIAdvisorService:

    @staticmethod
    def get_advice(
        portfolio_id: str
    ):

        analytics = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        recommendations = []

        roi = analytics.get(
            "portfolio_roi_percent",
            0
        )

        holdings = analytics.get(
            "holdings",
            []
        )

        if roi < 0:

            recommendations.append(
                {
                    "type": "SELL_REVIEW",
                    "message":
                    "Portfolio is currently underperforming."
                }
            )

        if len(holdings) < 3:

            recommendations.append(
                {
                    "type": "DIVERSIFY",
                    "message":
                    "Increase diversification across sectors."
                }
            )

        for holding in holdings:

            if holding["roi_percent"] > 15:

                recommendations.append(
                    {
                        "type": "TAKE_PROFIT",
                        "symbol":
                        holding["symbol"],
                        "message":
                        f"Consider taking profit on {holding['symbol']}."
                    }
                )

            elif holding["roi_percent"] < -10:

                recommendations.append(
                    {
                        "type": "RISK_WARNING",
                        "symbol":
                        holding["symbol"],
                        "message":
                        f"{holding['symbol']} is showing significant losses."
                    }
                )

        return {

            "portfolio_id":
                portfolio_id,

            "portfolio_roi":
                roi,

            "recommendations":
                recommendations
        }