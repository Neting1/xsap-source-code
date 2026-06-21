from app.services.intelligence_engine import (
    IntelligenceEngine
)


class RecommendationEngine:

    @staticmethod
    def get_recommendations(
        portfolio_id: str
    ):

        intelligence = (
            IntelligenceEngine
            .get_portfolio_intelligence(
                portfolio_id
            )
        )

        recommendations = []

        if (
            intelligence[
                "diversification_score"
            ] < 40
        ):

            recommendations.append(
                {
                    "type":
                        "Diversification",

                    "message":
                        "Increase the number of stocks in the portfolio."
                }
            )

        if (
            intelligence[
                "risk_level"
            ] == "High"
        ):

            recommendations.append(
                {
                    "type":
                        "Risk",

                    "message":
                        "Current portfolio risk is high."
                }
            )

        exposure = (
            intelligence[
                "sector_exposure"
            ]
        )

        telecom = exposure.get(
            "Telecom",
            0
        )

        if telecom > 50:

            recommendations.append(
                {
                    "type":
                        "Sector",

                    "message":
                        "Reduce Telecom concentration and increase Banking exposure."
                }
            )

        loser = (
            intelligence[
                "top_loser"
            ]
        )

        if loser:

            recommendations.append(
                {
                    "type":
                        "Review",

                    "message":
                        f"Review {loser['symbol']} due to underperformance."
                }
            )

        if not recommendations:

            recommendations.append(
                {
                    "type":
                        "Healthy",

                    "message":
                        "Portfolio allocation appears balanced."
                }
            )

        return {

            "portfolio_id":
                portfolio_id,

            "health_score":
                intelligence[
                    "health_score"
                ],

            "risk_level":
                intelligence[
                    "risk_level"
                ],

            "recommendations":
                recommendations
        }