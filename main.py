from fastapi import FastAPI
import uuid

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from firebase_admin import firestore
from starlette.background import BackgroundTasks

from crud_PEG import *
from crud_operations import *
from models import *
from generateXL import complete_PEG
from send_email import send_email_async, send_email_background
from fastapi import FastAPI, File, UploadFile

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
    organisational_assignment: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/getUser")
def get_user_by_id(id: str):
    return get_user(id)


@app.get("/getAllUsers")
def get_all_feedbacks():
    allUsers = []
    users = db.collection(u'users').stream()
    for u in users:
        allUsers.append(u.to_dict())
    return allUsers


@app.post("/addUser")
def post_add(obj: User_Item):
    add_user(obj, obj.id)
    return {"message": "user added"}


@app.post("/updateUser")
def post_update(obj: User_Item):
    return update_user(obj.id, obj)


@app.delete("/deleteUser")
def delete(id: str):
    delete_user(id)
    return {"message": "user deleted"}


@app.get("/getAllUsers")
def get_all():
    return get_all_users()

@app.post("/addPeg")
def post_peg(obj: PEG_Item):
    add_peg(obj)
    return {"message": "peg added"}


@app.get("/allPegs")
def get_pegs():
    return get_all_pegs()


@app.get("/getPeg")
def get_peg_by_id(id: str):
    return get_peg(id)


@app.delete("/deletePeg")
def delete_peg_by_id(id: str):
    delete_peg(id)
    return {'message': 'PEG deleted'}

@app.get("/getFeedback")
def get_feedback_by_id(id: str):
    return get_feedback(id)


@app.get("/getAllFeedback")
def get_all_feedbacks():
    allFeedbacks = []
    feedbacks = db.collection(u'feedback').order_by("timestamp").stream()
    for f in feedbacks:
        allFeedbacks.append(f.to_dict())
    return allFeedbacks


@app.post("/addFeedback")
def post_add_feedback(obj: Feedback_Item):
    my_obj = {
        "from_user_id": obj.from_user_id,
        "to_user_id": obj.to_user_id,
        "status": obj.status,
        "project_id": obj.project_id,
        "anonym": obj.anonym,
        "category": obj.category,
        "timestamp": firestore.SERVER_TIMESTAMP,
        "uid": uuid.uuid4().hex,
        "text": obj.text
    }
    add_feedback(my_obj)
    return {"message": "feedback added"}


@app.post("/updateFeedback")
def post_update_feedback(from_user_id: str, to_user_id: str, status: str, project_id: str, anonym: bool,
                         list_of_categories: List[str], feedback_date: date):
    date_of_feedback = feedback_date.strftime("%m-%d-%Y")
    date = datetime.datetime.strptime(date_of_feedback, "%m-%d-%Y")
    time_tuple = date.timetuple()
    timestamp = time.mktime(time_tuple)

    return update_feedback(id, {"from_user_id": from_user_id, "to_user_id": to_user_id, "status": status,
                                "project_id": project_id, "anonym": anonym, "list_of_categories": list_of_categories,
                                "feedback_date": timestamp})


@app.delete("/deleteFeedback")
def delete_Feedback(id: str):
    delete_feedback(id)
    return {"message": "user deleted"}


# 2 endpointuri ca-s 2 metode diferite, fac acelasi lucru
# /send-email/backgroundtasks merge mai rapid
@app.get('/send-email/asynchronous')
async def send_email_asynchronous():
    #with open("PEGS.xlsx", "rb") as data:
    await send_email_async('PEG received', 'bogdan_mozacu@yahoo.com',
                           "request", UploadFile("PEGS.xlsx"))
    return 'Success'


@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks, 'PEG received',
                          'calin_calinnemes@yahoo.com', "request mail")
    return 'Success'

@app.get('/XLgenerator')
def generateXLFile(id_peg: str):
    complete_PEG(id_peg)

