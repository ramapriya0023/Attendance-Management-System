from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/LeaveApplication")
database = client.LeaveApplication
leavelogdb = database.get_collection("LeaveLog")
leavedb=database.get_collection("AppliedLeave")