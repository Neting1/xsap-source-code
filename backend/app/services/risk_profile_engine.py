from app.repositories.portfolio_repository import (
    PortfolioRepository
)

from app.services.analytics_engine import (
    AnalyticsEngine
)

from app.services.forecasting_engine import (
    ForecastingEngine
)


class RiskProfileEngine:

    @staticmethod
    def assess_investor(
        investor_id: str
    ):

        portfolios = (
            PortfolioRepository
            .get_portfolios_by_investor(
                investor_id
            )
        )

        total_score = 0
        portfolio_count = 0

        for portfolio in portfolios:

            portfolio_id = (
                portfolio.get(
                    "portfolio_id"
                )
            )

            risk = (
                AnalyticsEngine
                .get_risk_analysis(
                    portfolio_id
                )
            )

            forecast = (
                ForecastingEngine
                .portfolio_forecast(
                    portfolio_id
                )
            )

            diversification = (
                risk.get(
                    "diversification_score",
                    0
                )
            )

            growth = (
                forecast.get(
                    "expected_growth_percent",
                    0
                )
            )

            score = (
                diversification
                +
                (growth * 10)
            )

            total_score += score
            portfolio_count += 1

        if portfolio_count == 0:

            return {

                "investor_id":
                    investor_id,

                "risk_profile":
                    "Conservative",

                "suitability_score":
                    0,

                "recommended_strategy":
                    "Defensive Investing"
            }

        suitability_score = round(
            total_score
            / portfolio_count,
            2
        )

        if suitability_score < 40:

            risk_profile = (
                "Conservative"
            )

            strategy = (
                "Defensive Investing"
            )

        elif suitability_score < 70:

            risk_profile = (
                "Moderate"
            )

            strategy = (
                "Balanced Investing"
            )

        else:

            risk_profile = (
                "Aggressive"
            )

            strategy = (
                "Growth Investing"
            )

        return {

            "investor_id":
                investor_id,

            "risk_profile":
                risk_profile,

            "suitability_score":
                suitability_score,

            "recommended_strategy":
                strategy
        }

    @staticmethod
    def check_portfolio_compatibility(
        investor_id: str,
        portfolio_id: str
    ):

        profile = (
            RiskProfileEngine
            .assess_investor(
                investor_id
            )
        )

        risk = (
            AnalyticsEngine
            .get_risk_analysis(
                portfolio_id
            )
        )

        portfolio_risk = (
            risk.get(
                "risk_level",
                "Low"
            )
        )

        investor_profile = (
            profile[
                "risk_profile"
            ]
        )

        compatible = True
        reason = (
            "Portfolio matches investor profile"
        )

        if (
            investor_profile
            == "Conservative"
            and portfolio_risk
            == "High"
        ):

            compatible = False

            reason = (
                "High-risk portfolio unsuitable for conservative investor"
            )

        elif (
            investor_profile
            == "Moderate"
            and portfolio_risk
            == "High"
        ):

            compatible = False

            reason = (
                "Portfolio risk exceeds moderate tolerance"
            )

        return {

            "portfolio_id":
                portfolio_id,

            "investor_id":
                investor_id,

            "compatible":
                compatible,

            "reason":
                reason
        }