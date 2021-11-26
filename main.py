from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
import time

from firebase import db
from crud_operations import *
from pydantic import BaseModel
from crud_PEG import *



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
    name: str
    username: str
    email: str
    role: str
    fiscal_year: int
    personal_number: str
    career_level: str
    organisational_assigment: str


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
def post_add(name: str, username: str, email: str, role: str, fiscal_year: int, personal_number: str, career_level: str, organisational_assigment: str, uid: str):
    add_user({"name":name,"username":username,"email":email,"role":role,"fiscal year":fiscal_year,"personal number":personal_number,"career level":career_level,"organisational assigment":organisational_assigment}, uid)
    return {"message":"user added"}

@app.post("/updateUser")
def post_update(obj:User_Item):
    return update_user(obj.id, {"name":obj.name,"username":obj.username,"email":obj.email,"role":obj.role,"fiscal year":obj.fiscal_year,"personal number":obj.personal_number,"career level":obj.career_level,"organisational assigment":obj.organisational_assigment})

@app.delete("/deleteUser")
def delete(id:str):
    delete_user(id)
    return {"message":"user deleted"}

@app.post("/addPeg")
def post_peg(obj: PEG_Item):
    add_peg(obj)
    return {"message":"peg added"}

@app.get("/allPegs")
def get_pegs():
    return get_all_pegs()

@app.get("/getPeg")
def get_peg_by_id(id:str):
    return get_peg(id)

@app.delete("/deletePeg")
def delete_peg_by_id(id: str):
    delete_peg(id)
    return {'message': 'PEG deleted'}