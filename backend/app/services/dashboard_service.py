from app.repositories.portfolio_repository import (
    PortfolioRepository
)

from app.repositories.notification_repository import (
    NotificationRepository
)

from app.repositories.alert_repository import (
    AlertRepository
)

from app.services.analytics_engine import (
    AnalyticsEngine
)


class DashboardService:

    @staticmethod
    def get_investor_dashboard(
        investor_id: str
    ):

        portfolios = (
            PortfolioRepository
            .get_all_portfolios()
        )

        investor_portfolios = [

            portfolio

            for portfolio in portfolios

            if portfolio.get(
                "investor_id"
            ) == investor_id
        ]

        portfolio_summaries = []

        risk_summaries = []

        top_performers = []

        for portfolio in investor_portfolios:

            portfolio_id = (
                portfolio[
                    "portfolio_id"
                ]
            )

            portfolio_summary = (
                AnalyticsEngine
                .get_portfolio_summary(
                    portfolio_id
                )
            )

            risk_summary = (
                AnalyticsEngine
                .get_risk_analysis(
                    portfolio_id
                )
            )

            performers = (
                AnalyticsEngine
                .get_top_performers(
                    portfolio_id
                )
            )

            portfolio_summaries.append(
                portfolio_summary
            )

            risk_summaries.append(
                risk_summary
            )

            top_performers.extend(
                performers
            )

        notifications = (
            NotificationRepository
            .get_user_notifications(
                investor_id
            )
        )

        alerts = (
            AlertRepository
            .get_user_alerts(
                investor_id
            )
        )

        return {

            "investor_id":
                investor_id,

            "portfolios_count":
                len(
                    investor_portfolios
                ),

            "portfolio_summary":
                portfolio_summaries,

            "risk_analysis":
                risk_summaries,

            "notifications_count":
                len(
                    notifications
                ),

            "alerts_count":
                len(
                    alerts
                ),

            "top_performers":
                top_performers
        }