from fastapi import APIRouter

from schemas.WorkHoursSchema import (
    create_checkin_user,
    doing_checkout_user
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
    