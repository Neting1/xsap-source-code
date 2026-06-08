from pydantic import BaseModel


class InvestorDashboardResponse(
    BaseModel
):
    investor_id: str
    total_portfolios: int
    total_holdings: int
    total_investment: float
    current_market_value: float
    profit_loss: float
    roi_percentage: float