from pydantic import BaseModel


class StrategySimulationRequest(
    BaseModel
):
    symbol: str
    buy_price: float
    sell_price: float
    capital: float


class StrategySimulationResponse(
    BaseModel
):
    symbol: str
    capital: float
    shares_bought: float
    final_value: float
    profit: float
    roi_percent: float


class StrategyPerformanceResponse(
    BaseModel
):
    symbol: str
    total_trades: int
    winning_trades: int
    losing_trades: int
    win_rate: float
    roi_percent: float