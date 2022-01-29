from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from schemas.userSchema import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from models.User import (
    ErrorResponseModel,
    ResponseModel,
    UpdateUser,
    User,
)

router = APIRouter()


@router.post("/", response_description="user data added into the database")
def add_user_data(user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user =  add_user(user)
    return ResponseModel(new_user, "user added successfully.")


@router.get("/", response_description="users retrieved")
def get_users():
    users =  retrieve_users()
    if users:
        return ResponseModel(users, "users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", response_description="user data retrieved")
def get_user_data(id):
    user =  retrieve_user(id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")


@router.put("/{id}")
def update_user_data(id: str, req: UpdateUser = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user =  update_user(id, req)
    if updated_user:
        return ResponseModel(
            "user with ID: {} name update is successful".format(id),
            "user name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


@router.delete("/{id}", response_description="user data deleted from the database")
def delete_user_data(id: str):
    deleted_user =  delete_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "user deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )
