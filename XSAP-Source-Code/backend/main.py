from fastapi import FastAPI

from app.api.v1.auth import (router as auth_router)
from app.api.v1.admin import (router as admin_router)
from app.api.v1.investors import (router as investor_router)
from app.api.v1.portfolio import (router as portfolio_router)
from app.api.v1.stocks import (router as stocks_router)
from app.api.v1.transactions import (router as transaction_router)
from app.api.v1.analytics import (router as analytics_router)
from app.api.v1.dashboard import (router as dashboard_router)
from app.api.v1.allocation import (router as allocation_router)
from app.api.v1.watchlist import (router as watchlist_router)
from app.api.v1.market import (router as market_router)
from app.api.v1.live_portfolio import (router as live_portfolio_router)
from app.api.v1.alerts import (router as alerts_router)


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





@app.get("/")
def root():

    return {
        "message":
        "XSAP API Running"
    }