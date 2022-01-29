from datetime import date
from operator import eq
from typing import Optional
from xmlrpc.client import boolean

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id:str=Field(...)
    autoid: str=Field(...)
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    #phonenumber: int = Field(...)
    dob: date = Field(...)
    experiance: int = Field(...)
    status:boolean= Field(...)
    roles: list =Field(...)
    #totalleaves:int =Field(...)
    

    


class UpdateUser(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
   # phonenumber: Optional[int ]
    #dob: Optional[date ]
    experiance: Optional[int ]
    status:Optional[boolean]
  

   


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
