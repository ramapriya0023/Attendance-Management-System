from pydantic import BaseModel
from typing import Optional

class ApplyLeave(BaseModel):
    id: str
    firstName: str
    reason: str
    status: Optional[str]

class LeaveReport(BaseModel):
    id: str
    firstName: str
    paidleave: int
    medicalleave: int
    privilegeleave: int
    lossofpay: int