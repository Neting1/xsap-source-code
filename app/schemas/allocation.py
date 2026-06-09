from pydantic import BaseModel
from typing import List


class AllocationItem(BaseModel):
    symbol: str
    market_value: float
    allocation_percentage: float


class AllocationResponse(BaseModel):
    portfolio_id: str
    allocations: List[AllocationItem]