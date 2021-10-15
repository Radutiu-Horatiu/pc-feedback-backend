from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from firebase import db

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
def get_test():
    # example to query database from FastAPI
    db.collection(u'test').document(u"ceva").set({"test":"test"})
    
    return {"text":"This is a get request from FastAPI."}