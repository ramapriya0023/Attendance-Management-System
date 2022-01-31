from pydantic import BaseModel
from typing import Optional

class ApplyLeave(BaseModel):
    autoid: str
    reason: str
    status: Optional[str]

class LeaveReport(BaseModel):
    autoid: str
    name: str
    paidleave: int
    medicalleave: int
    privilegeleave: int
    lossofpay: int