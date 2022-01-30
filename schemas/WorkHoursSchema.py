from asyncio.windows_events import NULL
import datetime as datr
from xmlrpc.client import DateTime
from bson.objectid import ObjectId
from config.db import userdb
from config.db import workhrs
from models.WorkingHoursModels import CheckIn



def user_helper(user) -> dict:
    return {
        "autoid":user["autoid"],
        "fullname": user["name"],
        "checkin": user["checkin"],
        "checkout":user["checkout"],
        "hours":user["hours"],
        "minutes":user["minutes"],
        "seconds":user["seconds"]        
    }

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

def calculate_working_hours(id:str):
    user = workhrs.find_one({"autoid":id})
    time_elapsed = user["checkout"]-user["checkin"]
    seconds = time_elapsed.total_seconds()
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(hour)
    print(minutes)
    print(seconds)
    data = {"hours":hour,"minutes":minutes,"seconds":seconds}
    workhrs.update_one({"autoid":id},{"$set":data})
    return "Hours : "+str(hour)+", Minutes : "+str(minutes)+", Seconds : "+str(seconds)

def report_work_hours(id:str) -> dict:
    user =  workhrs.find_one({"autoid": id})
    if user:
        return user_helper(user)
    
    