from pydantic import BaseModel


class SystemStatisticsResponse(BaseModel):

    total_investors: int
    total_portfolios: int
    total_transactions: int
    total_holdings: int
    total_alerts: int