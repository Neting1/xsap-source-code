from pydantic import BaseModel
from typing import Optional


class UserModel(BaseModel):
    uid: str
    full_name: str
    email: str
    role: str
    status: str