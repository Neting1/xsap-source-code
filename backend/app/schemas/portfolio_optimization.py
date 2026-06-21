from pydantic import BaseModel
from typing import Dict
from typing import List


class PortfolioOptimizationResponse(
    BaseModel
):

    portfolio_id: str
    efficiency_score: float
    optimization_status: str

    current_allocation: Dict[
        str,
        float
    ]

    target_allocation: Dict[
        str,
        float
    ]

    recommended_actions: List[
        str
    ]