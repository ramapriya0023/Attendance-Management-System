from fastapi import FastAPI
from routes.ApplyLeave import leaveroute 
app = FastAPI()
app.include_router(leaveroute)