from pydantic import BaseModel


class AlertResponse(BaseModel):

    alert_type: str
    severity: str
    message: str