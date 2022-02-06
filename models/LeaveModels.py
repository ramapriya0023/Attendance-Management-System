#author Ramapriya R

from pydantic import BaseModel
from typing import Optional

class ApplyLeave(BaseModel):
    empid: str
    leaveid:str
    reason: str
    status: Optional[str]

class LeaveReport(BaseModel):
    empid: str
    name: str
    paidleave: int
    medicalleave: int
    privilegeleave: int
    lossofpay: int