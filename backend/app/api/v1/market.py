from fastapi import APIRouter

from app.services.providers.gse_provider import (GSEProvider)
from app.services.market_sync_service import (sync_gse_market)

router = APIRouter(
    prefix="/market",
    tags=["Market Data"]
)

provider = GSEProvider()


@router.get("/gse")
def get_gse_market():

    return provider.get_all_stocks()

@router.post("/sync")
def sync_market():

    return sync_gse_market()

@router.get("/gse/{symbol}")
def get_gse_stock(
    symbol: str
):

    return provider.get_stock(
        symbol.upper()
    )