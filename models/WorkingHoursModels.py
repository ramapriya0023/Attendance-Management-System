import datetime
from pydantic import BaseModel

class WorkingHours(BaseModel):
    autoid: str

class CheckIn():
    def __init__(self,autoid,name,checkin):
        self.autoid =  autoid
        self.name = name
        self.checkin = checkin

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

    