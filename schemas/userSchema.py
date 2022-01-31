
from bson.objectid import ObjectId
from config.db import userdb
from schemas.idGenerator import Resource


# helpers


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "autoid":user["autoid"],
        "fullname": user["fullname"],
        "email": user["email"],
        
        "dob":user["dob"],
        "experiance":user["experiance"],
        "status":user["status"],
        "roles":user["roles"],
        
        
    }

#"phonenumber": user["phonenumber"],"totalleaves":user["totalleaves"],
# crud operations

# Retrieve all users present in the database
def retrieve_users():
    users = []
    for user in userdb.find():
        users.append(user_helper(user))
    return users


# Add a new user into to the database
def add_user(user_data: dict) -> dict:
    #user_data.__setitem__("autoid",Resource)
    user =  userdb.insert_one(user_data)
    new_user =  userdb.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a user with a matching ID
def retrieve_user(id: str) -> dict:
    user =  userdb.find_one({"autoid": id})
    if user:
        return user_helper(user)


# Update a user with a matching ID
def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user =  userdb.find_one({"autoid": id})
    if user:
        updated_user =  userdb.update_one(
            {"autoid": id}, {"$set": data}
        )
        if updated_user:
            return True
        return False

# Delete a user from the database
def delete_user(id: str):
    user =  userdb.find_one({"autoid": id})
    if user:
        userdb.delete_one({"autoid": id})
        return True
