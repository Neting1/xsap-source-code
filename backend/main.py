from fastapi import FastAPI

from app.api.v1.auth import (router as auth_router)
from app.api.v1.admin import (router as admin_router)
from app.api.v1.investors import (router as investor_router)
from app.api.v1.portfolio import (router as portfolio_router)
from app.api.v1.stocks import (router as stocks_router)
from app.api.v1.holdings import (router as holdings_router)
from app.api.v1.transactions import (router as transaction_router)
from app.api.v1.analytics import (router as analytics_router)
from app.api.v1.dashboard import (router as dashboard_router)
from app.api.v1.allocation import (router as allocation_router)
from app.api.v1.watchlist import (router as watchlist_router)
from app.api.v1.market import (router as market_router)
from app.api.v1.live_portfolio import (router as live_portfolio_router)
from app.api.v1.alerts import (router as alerts_router)
from app.api.v1.notifications import (router as notifications_router)
from app.api.v1.email import (router as email_router)
from app.api.v1.intelligence import (router as intelligence_router)
from app.api.v1.recommendations import (router as recommendations_router)
from app.api.v1.executive_dashboard import (router as executive_dashboard_router)
from app.api.v1.reports import (router as reports_router)
from app.api.v1.advisor import (router as advisor_router)
from app.api.v1.watchlist_analytics import (router as watchlist_analytics_router)
from app.api.v1.strategy import (router as strategy_router)
from app.api.v1.forecasting import (router as forecasting_router)
from app.api.v1.alerts_engine import (router as alerts_engine_router)
from app.api.v1.market_intelligence import (router as market_intelligence_router)
from app.api.v1.rebalancing import (router as rebalancing_router)
from app.api.v1.risk_profile import (router as risk_profile_router)
from app.api.v1.investment_strategy import (router as investment_strategy_router)
from app.api.v1.portfolio_optimization import (router as portfolio_optimization_router)




app = FastAPI(
    title="Xeonsys Stock Analytics Platform",
    version="1.0.0"
)


# Authentication
app.include_router(auth_router)
# Admin
app.include_router(admin_router)
# Investors
app.include_router(investor_router)
# Portfolio
app.include_router(portfolio_router)
# Stocks
app.include_router(stocks_router)
# Transactions
app.include_router(transaction_router)
# Analytics
app.include_router(analytics_router)
# Dashboard
app.include_router(dashboard_router,prefix="/api/v1")
# Allocation Analytics
app.include_router(allocation_router,prefix="/api/v1")
# Watchlist
app.include_router(watchlist_router,prefix="/api/v1")
# Market Data (GSE)
app.include_router(market_router,prefix="/api/v1")
# Live Portfolio
app.include_router(live_portfolio_router,prefix="/api/v1")
# Alerts
app.include_router(alerts_router,prefix="/api/v1")
# Notifications
app.include_router(notifications_router)
# Email
app.include_router(email_router)
# Holdings
app.include_router(holdings_router,prefix="/api/v1")
# Intelligence
app.include_router(intelligence_router,prefix="/api/v1")
# Recommendations
app.include_router(recommendations_router,prefix="/api/v1")
# Executive Dashboard
app.include_router(executive_dashboard_router,prefix="/api/v1")
# Reports
app.include_router(reports_router,prefix="/api/v1")
# Advisor
app.include_router(advisor_router,prefix="/api/v1")
# Watchlist Analytics
app.include_router(watchlist_analytics_router,prefix="/api/v1")
# Strategy
app.include_router(strategy_router,prefix="/api/v1")
# Forecasting
app.include_router(forecasting_router,prefix="/api/v1")
# Alerts Engine
app.include_router(alerts_engine_router,prefix="/api/v1")
# Market Intelligence
app.include_router(market_intelligence_router,prefix="/api/v1")
# Rebalancing
app.include_router(rebalancing_router,prefix="/api/v1")
# Risk Profile
app.include_router(risk_profile_router,prefix="/api/v1")
# Investment Strategy
app.include_router(investment_strategy_router,prefix="/api/v1")
# Portfolio Optimization
app.include_router(portfolio_optimization_router,prefix="/api/v1")


@app.get("/")
def root():

    return {
        "message":
        "XSAP API Running"
    }