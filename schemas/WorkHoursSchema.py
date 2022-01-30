from asyncio.windows_events import NULL
import datetime as datr
from xmlrpc.client import DateTime
from bson.objectid import ObjectId
from config.db import userdb
from config.db import workhrs
from models.WorkingHoursModels import CheckIn



# def user_helper(user) -> dict:
#     return {
#         "autoid":user["autoid"],
#         "fullname": user["fullname"],
#         "checkin": user["checkin"]        
#     }

def create_checkin_user(id:str):
    user = userdb.find_one({"autoid":id})
    if(workhrs.find_one({"autoid":id})):
        data = {"checkin":datr.datetime.now()}
        workhrs.update_one({"autoid":id},{"$set":data})
    else:
        workhrs.insert_one({"autoid":id,"name":user["fullname"],"checkin":datr.datetime.now()})
    
    return id+" Checked-in successfully."

def doing_checkout_user(id:str):
    user = workhrs.find_one({"autoid":id})
    if user:
        data = {"checkout":datr.datetime.now()}
        updated_user = workhrs.update_one({"autoid":id},{"$set":data})
    return id+" Checkedout successfully"

    
    