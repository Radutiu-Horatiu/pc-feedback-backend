from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
import time

from firebase import db
from crud_operations import *
from pydantic import BaseModel
from crud_PEG import *

from models import *


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

class Dummy_User_Item(BaseModel):
    name: str
    uid: str
    email: str

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
def post_add(obj:Dummy_User_Item):
    add_user({"name":obj.name,"email":obj.email}, obj.uid)
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

@app.get("/getFeedback")
def get_feedback_by_id(id:str):
    return get_feedback(id)

@app.post("/addFeedback")
def post_add_feedback(from_user_id: str, to_user_id: str , status: str, project_id: str, anonym:bool, list_of_categories:List[str], feedback_date: date):
    date_of_feedback = feedback_date.strftime("%m-%d-%Y")
    date = datetime.datetime.strptime(date_of_feedback, "%m-%d-%Y")
    time_tuple = date.timetuple()
    timestamp = time.mktime(time_tuple)


    add_feedback({"from_user_id": from_user_id, "to_user_id":to_user_id, "status":status, "project_id": project_id, "anonym":anonym, "list_of_categories":list_of_categories, "feedback_date":timestamp})
    return {"message":"user added"}

@app.post("/updateFeedback")
def post_update_feedback(from_user_id: str, to_user_id: str , status: str, project_id: str, anonym:bool, list_of_categories:List[str], feedback_date: date):

    date_of_feedback = feedback_date.strftime("%m-%d-%Y")
    date = datetime.datetime.strptime(date_of_feedback, "%m-%d-%Y")
    time_tuple = date.timetuple()
    timestamp = time.mktime(time_tuple)


    return update_feedback(id, {"from_user_id": from_user_id, "to_user_id":to_user_id, "status":status, "project_id": project_id, "anonym":anonym, "list_of_categories":list_of_categories, "feedback_date":timestamp})

@app.delete("/deleteFeedback")
def delete_Feedback(id:str):
    delete_feedback(id)
    return {"message":"user deleted"}