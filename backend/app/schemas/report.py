from pydantic import BaseModel
from typing import List, Dict, Any


class PortfolioReportResponse(BaseModel):

    portfolio_id: str

    analytics: Dict[str, Any]

    intelligence: Dict[str, Any]

    recommendations: Dict[str, Any]


class InvestorStatementResponse(BaseModel):

    investor_id: str

    total_portfolios: int

    total_market_value: float

    total_profit_loss: float

    total_roi_percent: float