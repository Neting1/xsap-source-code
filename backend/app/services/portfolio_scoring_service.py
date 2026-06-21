from app.services.analytics_engine import (
    AnalyticsEngine
)


class PortfolioScoringService:

    @staticmethod
    def calculate_score(
        portfolio_id: str
    ):

        analytics = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        holdings = analytics.get(
            "holdings",
            []
        )

        score = 100

        if len(holdings) < 3:
            score -= 20

        roi = analytics.get(
            "portfolio_roi_percent",
            0
        )

        if roi < 0:
            score -= 15

        if roi > 10:
            score += 5

        score = max(
            0,
            min(score, 100)
        )

        return {
            "portfolio_id": portfolio_id,
            "score": score
        }