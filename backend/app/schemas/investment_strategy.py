from pydantic import BaseModel
from typing import Dict


class InvestmentStrategyResponse(
    BaseModel
):

    investor_id: str
    risk_profile: str
    recommended_strategy: str
    allocation_plan: Dict[str, float]
    investment_horizon: str
    expected_risk: str
    expected_return_range: str