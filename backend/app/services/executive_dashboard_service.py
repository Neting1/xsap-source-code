from app.core.firebase import db

from app.services.providers.gse_provider import (
    GSEProvider
)

from app.services.analytics_engine import (
    AnalyticsEngine
)


class ExecutiveDashboardService:

    @staticmethod
    def get_dashboard():

        investors = list(
            db.collection(
                "investors"
            ).stream()
        )

        portfolios = list(
            db.collection(
                "portfolios"
            ).stream()
        )

        transactions = list(
            db.collection(
                "transactions"
            ).stream()
        )

        holdings = list(
            db.collection(
                "holdings"
            ).stream()
        )

        alerts = list(
            db.collection(
                "price_alerts"
            ).stream()
        )

        notifications = list(
            db.collection(
                "notifications"
            ).stream()
        )

        total_aum = 0

        risk_stats = {
            "Low": 0,
            "Medium": 0,
            "High": 0
        }

        top_stocks = []

        provider = GSEProvider()

        for portfolio in portfolios:

            data = portfolio.to_dict()

            portfolio_id = data.get(
                "portfolio_id"
            )

            analytics = (
                AnalyticsEngine
                .get_portfolio_summary(
                    portfolio_id
                )
            )

            total_aum += analytics.get(
                "total_market_value",
                0
            )

        stocks = provider.get_all_stocks()

        if stocks:

            stocks = sorted(
                stocks,
                key=lambda x:
                float(
                    x.get(
                        "change_percent",
                        0
                    )
                ),
                reverse=True
            )

            top_stocks = stocks[:5]

        return {

            "total_investors":
                len(investors),

            "total_portfolios":
                len(portfolios),

            "total_transactions":
                len(transactions),

            "total_holdings":
                len(holdings),

            "total_assets_under_management":
                round(
                    total_aum,
                    2
                ),

            "active_alerts":
                len(alerts),

            "active_notifications":
                len(notifications),

            "market_summary":
                {
                    "listed_stocks":
                        len(stocks)
                        if stocks
                        else 0
                },

            "top_performing_stocks":
                top_stocks,

            "risk_distribution":
                risk_stats
        }