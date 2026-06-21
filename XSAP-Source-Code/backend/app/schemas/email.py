from pydantic import BaseModel, EmailStr


class EmailRequest(BaseModel):

    email: EmailStr


class AlertEmailRequest(BaseModel):

    email: EmailStr
    stock_symbol: str
    current_price: float