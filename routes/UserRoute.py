from fastapi import APIRouter, Query
from models.User import User
from models.User import ResponseModel
from models.User import UpdateUser

from config.db import userdb
from schemas.leaveschema import serializeDict, serializeList
from bson import ObjectId
user = APIRouter()

@user.post('/newuser')
async def new_user(usr: User):
    userdb.insert_one(dict(usr))
    data={"hi":"hello"}
    return ResponseModel(data,"New user added!")

@user.get('user/{id}')
async def get_user(id):
    return serializeDict(userdb.find_one({"_id":ObjectId(id)}))

# @user.put('user/{id}')
# async def approve_leave(id,status: str):
#     userdb.find_one_and_update({"_id":ObjectId(id)},{ "$set":{"status": status}})
#     return "Leave has been Approved"

@user.get('/allusers')
async def allusers():
    return serializeList(userdb.find())

@user.delete('user/{id}')
async def delete_user():
    userdb.find_one_and_delete({"_id":ObjectId(id)})
    return "User has been deleted."
