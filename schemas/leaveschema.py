from config.db import leavereportdb
from config.db import leavedb
from bson import ObjectId

def leaveEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "firstName":item["firstName"],
        "reason":item["reason"]
    }

def reportEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "firstName": item["firstName"],
        "paidLeave": item["paidLeave"],
        "medicalLeave": item["medicalLeave"],
        "privilegeLeave": item["privilegeLeave"],
        "lossofPay": item["lossofPay"]
    }
def leavesEntity(entity) -> list:
    if (leaveEntity):
        return [leaveEntity(item) for item in entity]
    else:
        return [reportEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]

def createReport(id):
    reportdict={}
    emp=leavedb.find_one({"_id":ObjectId(id)})
    reportdict["id"]=id
    reportdict["firstName"]=emp["firstName"]
    reportdict["paidleave"]=0
    reportdict["medicalleave"]=0
    reportdict["privilegeleave"]=0
    reportdict["lossofpay"]=0
    leavereportdb.insert_one(reportdict)

def updateReport(id,reason):
    empreport=leavereportdb.find_one({"_id":ObjectId(id)})
    #leavedb.find_one_and_update({"_id":ObjectId(id)},{ "$set":{"status": status}})
