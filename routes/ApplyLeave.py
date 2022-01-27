from fastapi import APIRouter, Query
from models.LeaveModels import ApplyLeave
from models.LeaveModels import LeaveTypes
from config.db import leavedb
from schemas.leaveschema import serializeDict, serializeList
from bson import ObjectId
leaveroute = APIRouter()

@leaveroute.post('/applyleave')
async def create_leave(leave: ApplyLeave):
    leavedb.insert_one(dict(leave))
    return "Leave applied"

@leaveroute.get('/{id}/leaveapplied')
async def get_leave(id):
    return serializeDict(leavedb.find_one({"_id":ObjectId(id)}))

@leaveroute.put('/{id}/approve')
async def approve_leave(id,status: str):
    leavedb.find_one_and_update({"_id":ObjectId(id)},{ "$set":{"status": status}})
    return "Leave has been Approved"

@leaveroute.get('/viewleaves')
async def view_leaves():
    return serializeList(leavedb.find())

@leaveroute.delete('/{id}/delete')
async def delete_leave():
    leavedb.find_one_and_delete({"_id":ObjectId(id)})
    return "Leave has been deleted"
