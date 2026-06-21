from pydantic import BaseModel
from typing import List


class RecommendationItem(BaseModel):

    type: str
    message: str


class RecommendationResponse(BaseModel):

    portfolio_id: str
    health_score: int
    risk_level: str
    recommendations: List[RecommendationItem]