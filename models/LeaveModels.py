from pydantic import BaseModel
from typing import Optional

class ApplyLeave(BaseModel):
    id: str
    firstName: str
    reason: str
    status: Optional[str]

class LeaveTypes(BaseModel):
    id: str
    firstName: str
    reason: str
    paidLeave: int
    medicalLeave: int
    privilegeLeave: int
    lossofPay: int