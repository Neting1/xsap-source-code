from pydantic import BaseModel


class StockForecastResponse(
    BaseModel
):
    symbol: str
    current_price: float
    predicted_price: float
    expected_return: float
    forecast: str
    confidence: float


class PortfolioForecastResponse(
    BaseModel
):
    portfolio_id: str
    current_value: float
    predicted_value: float
    expected_growth_percent: float