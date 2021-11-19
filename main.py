from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from firebase import db
from crud_operations import *
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class User_Item(BaseModel):
    id: str
    nume: str
    prenume: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
def get_test():
    # example to query database from FastAPI
    db.collection('test').document("ceva").set({"test":"test"})

    return {"text":"This is a get request from FastAPI."}

@app.get("/ceva")
def get_ceva():
    return {"ceva":"Asta e inca un test."}

@app.get("/getUser")
def get_user_by_id(id:str):
    return get_user(id)

@app.post("/addUser")
def post_add(nume:str, prenume:str):
    add_user({"nume":nume,"prenume":prenume})
    return {"message":"user added"}

@app.post("/updateUser")
def post_update(obj:User_Item):
    return update_user(obj.id, {"nume":obj.nume,"prenume":obj.prenume})

@app.delete("/deleteUser")
def delete(id:str):
    delete_user(id)
    return {"message":"user deleted"}

