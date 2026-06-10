from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.stock import (
    StockCreate,
    StockUpdate
)

from app.services.stock_service import (
    add_stock,
    fetch_all_stocks,
    fetch_stock,
    edit_stock,
    remove_stock
)

router = APIRouter(
    prefix="/api/v1/stocks",
    tags=["Stocks"]
)


@router.post("/")
def create_stock(
    stock: StockCreate
):

    return add_stock(
        stock.dict()
    )


@router.get("/")
def get_all_stocks():

    stocks = fetch_all_stocks()

    return {
        "total_stocks":
        len(stocks),
        "stocks":
        stocks
    }


@router.get("/{symbol}")
def get_stock_by_symbol(
    symbol: str
):

    stock = fetch_stock(
        symbol
    )

    if not stock:

        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return stock


@router.put("/{symbol}")
def update_stock_by_symbol(
    symbol: str,
    stock: StockUpdate
):

    existing = fetch_stock(
        symbol
    )

    if not existing:

        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return edit_stock(
        symbol,
        stock.dict(
            exclude_unset=True
        )
    )


@router.delete("/{symbol}")
def delete_stock_by_symbol(
    symbol: str
):

    existing = fetch_stock(
        symbol
    )

    if not existing:

        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return remove_stock(
        symbol
    )