from pydantic import BaseModel
from typing import List, Dict


class RebalancingAction(
    BaseModel
):
    action: str
    symbol: str | None = None
    sector: str | None = None
    reason: str


class RebalancingResponse(
    BaseModel
):
    portfolio_id: str
    current_risk: str
    current_diversification: float
    recommended_actions: List[Dict]