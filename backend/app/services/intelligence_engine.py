from app.services.analytics_engine import (
    AnalyticsEngine
)


class IntelligenceEngine:

    @staticmethod
    def get_portfolio_intelligence(
        portfolio_id: str
    ):

        portfolio = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        risk = (
            AnalyticsEngine
            .get_risk_analysis(
                portfolio_id
            )
        )

        holdings = portfolio.get(
            "holdings",
            []
        )

        diversification_score = (
            risk[
                "diversification_score"
            ]
        )

        health_score = (
            IntelligenceEngine
            .calculate_health_score(
                portfolio,
                risk
            )
        )

        grade = (
            IntelligenceEngine
            .calculate_grade(
                health_score
            )
        )

        sector_exposure = (
            IntelligenceEngine
            .sector_exposure(
                holdings
            )
        )

        top_gainer = (
            IntelligenceEngine
            .top_gainer(
                holdings
            )
        )

        top_loser = (
            IntelligenceEngine
            .top_loser(
                holdings
            )
        )

        recommendations = (
            IntelligenceEngine
            .recommendations(
                portfolio,
                risk
            )
        )

        return {

            "portfolio_id":
                portfolio_id,

            "health_score":
                health_score,

            "grade":
                grade,

            "risk_level":
                risk["risk_level"],

            "diversification_score":
                diversification_score,

            "sector_exposure":
                sector_exposure,

            "top_gainer":
                top_gainer,

            "top_loser":
                top_loser,

            "recommendations":
                recommendations
        }

    @staticmethod
    def calculate_health_score(
        portfolio,
        risk
    ):

        score = 100

        roi = portfolio.get(
            "portfolio_roi_percent",
            0
        )

        if roi < 0:

            score -= min(
                abs(int(roi)),
                30
            )

        score -= int(
            risk[
                "largest_position_percent"
            ] / 5
        )

        return max(score, 0)

    @staticmethod
    def calculate_grade(
        score
    ):

        if score >= 90:
            return "A"

        if score >= 80:
            return "B"

        if score >= 70:
            return "C"

        if score >= 60:
            return "D"

        return "F"

    @staticmethod
    def sector_exposure(
        holdings
    ):

        sector_map = {

            "MTNGH":
                "Telecom",

            "SIC":
                "Insurance",

            "GCB":
                "Banking",

            "CAL":
                "Banking",

            "SCB":
                "Banking",

            "GOIL":
                "Energy"
        }

        total = sum(
            h["market_value"]
            for h in holdings
        )

        sectors = {}

        for holding in holdings:

            sector = sector_map.get(
                holding["symbol"],
                "Other"
            )

            sectors[sector] = (
                sectors.get(
                    sector,
                    0
                )
                +
                holding[
                    "market_value"
                ]
            )

        result = {}

        for sector, value in sectors.items():

            percent = 0

            if total > 0:

                percent = round(
                    (
                        value / total
                    )
                    * 100,
                    2
                )

            result[sector] = percent

        return result

    @staticmethod
    def top_gainer(
        holdings
    ):

        if not holdings:
            return {}

        return max(
            holdings,
            key=lambda x:
            x["roi_percent"]
        )

    @staticmethod
    def top_loser(
        holdings
    ):

        if not holdings:
            return {}

        return min(
            holdings,
            key=lambda x:
            x["roi_percent"]
        )

    @staticmethod
    def recommendations(
        portfolio,
        risk
    ):

        recommendations = []

        if (
            risk[
                "largest_position_percent"
            ] > 50
        ):

            recommendations.append(
                "Portfolio concentration is high. Consider diversification."
            )

        if (
            portfolio[
                "portfolio_roi_percent"
            ] < 0
        ):

            recommendations.append(
                "Portfolio currently showing negative returns."
            )

        if (
            risk[
                "diversification_score"
            ] < 40
        ):

            recommendations.append(
                "Diversification score is low."
            )

        if not recommendations:

            recommendations.append(
                "Portfolio performance is healthy."
            )

        return recommendations