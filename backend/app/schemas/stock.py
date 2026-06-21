from pydantic import BaseModel
from typing import Optional


class StockCreate(BaseModel):
    symbol: str
    company_name: str
    sector: str
    market: str
    current_price: float


class StockUpdate(BaseModel):
    company_name: Optional[str] = None
    sector: Optional[str] = None
    market: Optional[str] = None
    current_price: Optional[float] = None
    status: Optional[str] = None