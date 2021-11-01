from typing import Optional
from fastapi import FastAPI, Path

app = FastAPI()

users = {
    1:{
        "name":"kdee",
        "email":"kdeemini@gmail.com",
        "age":21
    },
    2:{
        "name":"sally",
        "email":"sallyjacobs@gmail.com",
        "age":32
    },
    3:{
        "name":"Milly",
        "email":"millyrock@gmail.com",
        "age":32
    }
}
    


@app.get("/")
def index():
    return {"name":"Welcome to the fastapi dev"}

@app.get("/get-user/{user_id}")
def get_user(user_id: int=Path(None, description="Get user id of target user")):
    return users[user_id]
