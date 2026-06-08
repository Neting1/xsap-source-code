from pydantic import BaseModel
from pydantic import EmailStr


class InvestorCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    country: str


class InvestorResponse(BaseModel):
    investor_id: str
    full_name: str
    email: EmailStr
    phone: str
    country: str
    status: str