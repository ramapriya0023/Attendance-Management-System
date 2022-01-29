from fastapi import FastAPI
from routes.ApplyLeave import leaveroute
from routes.UserRoute import user
from routes.USER_ROUTE import router
app = FastAPI()
app.include_router(leaveroute)
#app.include_router(user)
app.include_router(router)