from pydantic import BaseModel
from typing import List, Dict


class IntelligenceResponse(BaseModel):

    portfolio_id: str

    health_score: int

    grade: str

    risk_level: str

    diversification_score: float

    sector_exposure: Dict

    top_gainer: Dict

    top_loser: Dict

    recommendations: List[str]