from pydantic import BaseModel


class RiskProfileResponse(
    BaseModel
):

    investor_id: str
    risk_profile: str
    suitability_score: float
    recommended_strategy: str


class PortfolioCompatibilityResponse(
    BaseModel
):

    portfolio_id: str
    investor_id: str
    compatible: bool
    reason: str