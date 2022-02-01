
from fastapi import APIRouter
from models.LeaveModels import ApplyLeave
from config.db import leavedb, leavereportdb
from models.User import ErrorResponseModel, ResponseModel
from schemas.leaveschema import (
    apply_leave,
    approving_leave,
    deleting_leave,
    generate_report,
    get_leaves,
    getting_leave
    )

leaveroute = APIRouter()

@leaveroute.post('/applyleave')
async def create_leave(leave: ApplyLeave):
    leave=apply_leave(dict(leave))
    return ResponseModel(leave, "leave applied successfully.")

@leaveroute.get('/leaveapplied/{autoid}')
async def get_leave(autoid):
    leave=getting_leave(autoid)
    if (leave):
        return ResponseModel(leave, "leave retrieved successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error retrieving the leave data.",
        ) 

@leaveroute.put('/approve/{autoid}')
async def approve_leave(autoid,status: str):
    leave=approving_leave(autoid,status)
    if (leave):
        return ResponseModel(leave, "leave approved successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error approving the leave.",
        ) 

@leaveroute.get('/viewleaves')
async def view_leaves():
    leaves=get_leaves()
    if (leaves):
        return ResponseModel(leaves, "leaves in the database retrieved successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error retrieving the leave datas.",
        ) 

@leaveroute.delete('/delete/{autoid}')
async def delete_leave(autoid):
    if(leavedb.find_one({"autoid":autoid})):
        deleting_leave(autoid)
        return ResponseModel("Leave id {}".format(autoid),"has been deleted successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error deleting the leave data.",
        ) 

@leaveroute.get('/report/{autoid}')
async def gen_report(autoid):
    report=generate_report(autoid)
    if (report):
        return ResponseModel(report, "Leave report generated successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error generating the leave reoprt.",
        ) 
    
    