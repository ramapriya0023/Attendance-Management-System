import logging
from config.db import leavereportdb
from config.db import leavedb
logging.basicConfig(level=logging.INFO)
def leaveEntity(item) -> dict:
    return {
        "empid":str(item["empid"]),
        "leaveid":str(item["leaveid"]),
        "reason":item["reason"],
        "status":item["status"]
    }

def reportEntity(item) -> dict:
    return{
        "empid":str(item["empid"]),
        "name": item["name"],
        "paidleave": item["paidleave"],
        "medicalleave": item["medicalleave"],
        "privilegeleave": item["privilegeleave"],
        "lossofpay": item["lossofpay"]
    }

def leavesEntity(entity) -> list:
    if (leaveEntity):
        return [leaveEntity(item) for item in entity]
    else:
        return [reportEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='id'},**{i:a[i] for i in a if i!='id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]

def createReport(id,name):
    reportdict={}
    reportdict["empid"]=id
    reportdict["name"]=name
    reportdict["paidleave"]=0
    reportdict["medicalleave"]=0
    reportdict["privilegeleave"]=0
    reportdict["lossofpay"]=0
    leavereportdb.insert_one(reportdict)

def updateReport(id,reason):
    logging.info("Updating the report")
    empreport=leavereportdb.find_one({"empid":id})
    empreport=dict(empreport)
    for key,value in empreport.items():
        if key==reason:
            num=value+1
    leavereportdb.find_one_and_update({"empid":id},{ "$set":{reason:num }})

def apply_leave(leave):
    logging.info("Applying the leave")
    leavedb.insert_one(leave)
    updateReport(leave["empid"],leave["reason"])
    return leave


def getting_leave(leaveid):
    logging.info("Retrieving the leave")
    return serializeDict(leavedb.find_one({"leaveid":leaveid}))
    

def approving_leave(leaveid,status):
    logging.info("Approving leave")
    leave= leavedb.find_one_and_update({"leaveid":leaveid},{ "$set":{"status": status}})
    return leave

def get_leaves():
    logging.info("Retrieving the leaves")
    leaves= serializeList(leavedb.find())
    return leaves

def deleting_leave(empid):
    logging.info("Deleting the leave")
    leavedb.find_one_and_delete({"empid":empid})

def generate_report(empid):
    logging.info("Inside report generation")
    val=leavereportdb.find_one({"empid":empid})
    return reportEntity(val)