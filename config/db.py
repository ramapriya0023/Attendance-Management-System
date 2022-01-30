from pymongo import MongoClient
#import motor.motor_asyncio
from bson.objectid import ObjectId
#from decouple import config
client=MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.76ha4.mongodb.net/AttendanceManagement?ssl=true&ssl_cert_reqs=CERT_NONE")
#MONGO_DETAILS = config("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.76ha4.mongodb.net/AttendanceManagement")
#client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.LeaveApplication
leavereportdb = database.get_collection("LeaveReports")
leavedb=database.get_collection("AppliedLeave")
userdb=database.get_collection("UserDb")
workhrs = database.get_collection("WorkingHours")