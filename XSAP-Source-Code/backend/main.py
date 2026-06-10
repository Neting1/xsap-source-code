from fastapi import FastAPI

from app.api.v1.admin import router as admin_router
from app.api.v1.alerts import router as alerts_router
from app.api.v1.allocation import router as allocation_router
from app.api.v1.analytics import router as analytics_router
from app.api.v1.auth import router as auth_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.email import router as email_router
from app.api.v1.investors import router as investors_router
from app.api.v1.live_portfolio import router as live_portfolio_router
from app.api.v1.market import router as market_router
from app.api.v1.notifications import router as notifications_router
from app.api.v1.portfolio import router as portfolio_router
from app.api.v1.stocks import router as stocks_router
from app.api.v1.transactions import router as transactions_router
from app.api.v1.watchlist import router as watchlist_router
from app.api.v1.market import (router as market_router)

app = FastAPI(
    title="Xeonsys Stock Analytics Platform API",
    description="Backend API for XSAP",
    version="1.0.0"
)

# Register routers
app.include_router(admin_router)
app.include_router(alerts_router)
app.include_router(allocation_router)
app.include_router(analytics_router)
app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(email_router)
app.include_router(investors_router)
app.include_router(live_portfolio_router)
app.include_router(market_router)
app.include_router(notifications_router)
app.include_router(portfolio_router)
app.include_router(stocks_router)
app.include_router(transactions_router)
app.include_router(watchlist_router)
app.include_router(market_router)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "XSAP API is running"
    }