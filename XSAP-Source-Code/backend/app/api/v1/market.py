from fastapi import APIRouter
from fastapi import HTTPException

from app.services.providers.gse_provider import (GSEProvider)
from app.services.market_sync_service import (sync_gse_market)

router = APIRouter(
    prefix="/market",
    tags=["Market Data"]
)

provider = GSEProvider()


@router.get("/gse")
def get_gse_market():

    data = provider.get_all_stocks()

    return {
        "total_stocks": len(data),
        "stocks": data
    }

@router.post("/sync")
def sync_market():

    return sync_gse_market()

@router.get("/gse/{symbol}")
def get_gse_stock(symbol: str):

    stock = provider.get_stock(
        symbol.upper()
    )

    if "error" in stock:

        raise HTTPException(
            status_code=404,
            detail=stock["error"]
        )

    return stock