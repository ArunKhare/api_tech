"""testing.py: Example FastAPI application for API testing."""

from sqlite3 import dbapi2
from fastapi import FastAPI
from pydantic import BaseModel
from collections import defaultdict

user_db = defaultdict(dict)
app = FastAPI()

user_db = {
    1: {"name": "John", "age": 30},
    2: {"name": "Jane", "age": 25},
    3: {"name": "Amrendra", "age": 22},
}


class User(BaseModel):
    name: str
    age: int

@app.get("/user_db/data/v1/get/{user_id}")
def get_user(user_id: int):
    if user_id in user_db:
        return {"user": user_db[user_id]}
    else:
        return {"error": "User not found"}

@app.put("/user_db/data/v1/update/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message": "User updated", "user": user_db[user_id]}
    else:
        return {"error": "User not found"}


@app.post("/user_db/data/v1/add/")
def add(usr_id: int, user: User):
    if usr_id in user_db:
        return {"error": "User ID already exists"}
    user_db[usr_id] = user.model_dump()
    print(user_db)
    return {"message": "User added", "user": user_db[usr_id]}


@app.delete("/user_db/data/v1/delete/")
def delete_item(item_id: int):
    if item_id in user_db:
        del user_db[item_id]
    else:
        return {"error": "Item not found"}
    print(user_db)
    return {"message": "Item deleted", "item_id": item_id}
