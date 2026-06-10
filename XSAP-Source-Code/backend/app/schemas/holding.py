from pydantic import BaseModel


class HoldingCreate(BaseModel):
    portfolio_id: str
    stock_symbol: str
    quantity: int
    average_price: float


class HoldingResponse(BaseModel):
    holding_id: str
    portfolio_id: str
    stock_symbol: str
    quantity: int
    average_price: float
    market_value: float