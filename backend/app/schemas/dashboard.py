from pydantic import BaseModel
from typing import List
from typing import Dict
from typing import Any


class PortfolioSummary(BaseModel):

    portfolio_id: str
    total_cost_basis: float
    total_market_value: float
    total_profit_loss: float
    portfolio_roi_percent: float


class RiskAnalysis(BaseModel):

    risk_level: str
    holdings_count: int
    largest_position_percent: float
    diversification_score: float


class InvestorDashboardResponse(BaseModel):

    investor_id: str

    portfolios_count: int

    portfolio_summary: List[
        PortfolioSummary
    ]

    risk_analysis: List[
        RiskAnalysis
    ]

    notifications_count: int

    alerts_count: int

    top_performers: List[
        Dict[str, Any]
    ]