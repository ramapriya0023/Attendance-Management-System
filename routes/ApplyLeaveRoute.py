from fastapi import APIRouter
from models.LeaveModels import ApplyLeave
from config.db import leavedb, leavereportdb
from schemas.leaveschema import serializeDict, serializeList, updateReport, reportEntity, leaveEntity
import logging

leaveroute = APIRouter()

@leaveroute.post('/applyleave')
async def create_leave(leave: ApplyLeave):
    
    leave=dict(leave)
    leavedb.insert_one(leave)
    print(leave)
    print(dict(leave))
    #print(leaveEntity(leave))
    
    updateReport(leave["autoid"],leave["reason"])
    return "Leave applied"

@leaveroute.get('/{autoid}/leaveapplied')
async def get_leave(autoid):
    return serializeDict(leavedb.find_one({"autoid":autoid}))

@leaveroute.put('/{autoid}/approve')
async def approve_leave(autoid,status: str):
    leavedb.find_one_and_update({"autoid":autoid},{ "$set":{"status": status}})
    return "Leave has been Approved"

@leaveroute.get('/viewleaves')
async def view_leaves():
    return serializeList(leavedb.find())

@leaveroute.delete('/{autoid}/delete')
async def delete_leave(autoid):
    leavedb.find_one_and_delete({"autoid":autoid})
    return "Leave has been deleted"

@leaveroute.get('/{autoid}/report')
async def gen_report(autoid):
    print("Insautoide report generation")
    logging.info("Insautoide report generation")
    #print (leavereportdb.find_one({"autoautoid":aautoid}))
    
    val=leavereportdb.find_one({"autoid":autoid})
    print(val)
    print("the end")
    return reportEntity(val)
    