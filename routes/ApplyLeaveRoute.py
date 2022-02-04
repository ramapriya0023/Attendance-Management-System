
from fastapi import APIRouter
from models.LeaveModels import ApplyLeave
from config.db import leavedb
from models.User import ErrorResponseModel, ResponseModel
from schemas.leaveschema import (
    apply_leave,
    approving_leave,
    deleting_leave,
    generate_report,
    get_leaves,
    getting_leave,
    leaveEntity,
    leavesEntity
    )

leaveroute = APIRouter()

@leaveroute.post('/applyleave')
async def create_leave(leave: ApplyLeave):
    leave=dict(leave)
    leave_created=apply_leave(leave)
    return ResponseModel(leaveEntity(leave_created), "leave applied successfully.")


@leaveroute.get('/leaveapplied/{leaveid}')
async def get_leave(leaveid):
    leave=getting_leave(leaveid)
    if (leave):
        return ResponseModel(leaveEntity(leave), "leave retrieved successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error retrieving the leave data.",
        ) 


@leaveroute.put('/approve/{leaveid}')
async def approve_leave(leaveid,status: str):
    leave=approving_leave(leaveid,status)
    if (leave):
        return ResponseModel(leaveEntity(leave), "leave approved successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error approving the leave.",
        ) 

@leaveroute.get('/leaveresponses')
async def leave_responses():
    leaves=get_leaves()
    if (leaves):
        return ResponseModel(leavesEntity(leaves), "leaves in the database retrieved successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error retrieving the leave datas.",
        ) 

@leaveroute.delete('/delete/{leaveid}')
async def delete_leave(leaveid):
    if(leavedb.find_one({"leaveid":leaveid})):
        deleting_leave(leaveid)
        return ResponseModel("Leave id {} has been deleted successfully.".format(leaveid),"Leave deleted successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error deleting the leave data.",
        ) 

@leaveroute.get('/report/{empid}')
async def gen_report(empid):
    report=generate_report(empid)
    if (report):
        return ResponseModel(report, "Leave report generated successfully.")
    else: 
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error generating the leave reoprt.",
        ) 
    
    