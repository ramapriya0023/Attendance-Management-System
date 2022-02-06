# author Vijayaraghavan D
from fastapi import APIRouter

from schemas.WorkHoursSchema import (
    create_checkin_user,
    doing_checkout_user,
    calculate_working_hours,
    report_work_hours
)

from models.WorkingHoursModels import (
    ErrorResponseModel,
    ResponseModel,
)

rou = APIRouter()

@rou.post('/checkin/{id}')
def check_in(id):
    checkin = create_checkin_user(id)
    return ResponseModel(checkin, "User checkin successfully")

@rou.put('/checkout/{id}')
def check_out(id):
    checkout = doing_checkout_user(id)
    return ResponseModel(checkout,"User checked-out successfully")

@rou.get('/workhours/{id}')
def work_hours(id):
    workhrs = calculate_working_hours(id)
    return ResponseModel(workhrs, "Work Hours calculated successfully")
    
@rou.get('/workhoursreport/{id}')
def report_of_working_hours(id):
    report = report_work_hours(id)
    return ResponseModel(report, "Report generated successfully")
