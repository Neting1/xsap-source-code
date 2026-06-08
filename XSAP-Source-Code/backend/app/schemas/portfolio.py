from pydantic import BaseModel
from typing import Optional


class PortfolioCreate(BaseModel):
    investor_id: str
    portfolio_name: str
    description: str


class PortfolioUpdate(BaseModel):
    portfolio_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None