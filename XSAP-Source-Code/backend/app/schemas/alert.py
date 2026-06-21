from pydantic import BaseModel


class AlertCreate(BaseModel):
    user_id: str
    stock_symbol: str
    condition: str
    target_price: float


class AlertResponse(BaseModel):
    alert_id: str
    user_id: str
    stock_symbol: str
    condition: str
    target_price: float
    status: str
    triggered: bool