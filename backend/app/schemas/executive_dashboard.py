from pydantic import BaseModel
from typing import List, Dict


class ExecutiveDashboardResponse(
    BaseModel
):

    total_investors: int

    total_portfolios: int

    total_transactions: int

    total_holdings: int

    total_assets_under_management: float

    active_alerts: int

    active_notifications: int

    market_summary: Dict

    top_performing_stocks: List

    risk_distribution: Dict