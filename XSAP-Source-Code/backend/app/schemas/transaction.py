from pydantic import BaseModel
from typing import Optional


class TransactionCreate(BaseModel):
    investor_id: str
    portfolio_id: str
    stock_symbol: str
    quantity: int
    price: float
    transaction_type: str


class TransactionResponse(BaseModel):
    transaction_id: str
    investor_id: str
    portfolio_id: str
    stock_symbol: str
    quantity: int
    price: float
    total_amount: float
    transaction_type: str
    status: str