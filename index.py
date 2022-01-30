from fastapi import FastAPI
from routes.ApplyLeave import leaveroute
from routes.UserRoute import user
from routes.USER_ROUTE import router
from routes.WorkHoursRoute import rou
app = FastAPI()
app.include_router(leaveroute)
#app.include_router(user)
app.include_router(router)
app.include_router(rou)