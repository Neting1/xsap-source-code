from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.admin import router as admin_router
from app.api.v1.investors import (router as investor_router)
from app.api.v1.portfolio import (router as portfolio_router)
from app.api.v1.stocks import (router as stocks_router)
from app.api.v1.transactions import (router as transaction_router)
from app.api.v1.analytics import (router as analytics_router)
from app.api.v1.dashboard import (router as dashboard_router)


app = FastAPI(title="Xeonsys Stock Analytics Platform",version="1.0.0")

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(investor_router)
app.include_router(portfolio_router)
app.include_router(stocks_router)
app.include_router(transaction_router)
app.include_router(analytics_router)
app.include_router(dashboard_router,prefix="/api/v1")



@app.get("/")
def root():
    return {
        "message": "XSAP API Running"
    }