from pydantic import BaseModel


class NotificationCreate(BaseModel):
    user_id: str
    title: str
    message: str
    type: str


class NotificationRead(BaseModel):
    notification_id: str
    user_id: str
    title: str
    message: str
    type: str
    read: bool
    created_at: str