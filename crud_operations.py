# Model..
from firebase import db

def getUserById(id):
  # return user specific to the id
  # db.collection('users').document("ceva").set({"test":"test"})

  # user from firestore
  user = {}

  return user

def get_user(id):
  user_ref = db.collection("users").document(id)
  return user_ref.get().to_dict()

def add_user(obj):
  db.collection("users").add(obj) 

def update_user(id, obj):
  print(obj)
  user_ref = db.collection("users").document(id)
  try:
    user_ref.update({"nume":obj["nume"], "prenume":obj["prenume"]})
    return {"message":"updated obj"}
  except:
    return {"error":"id dosent exist"}

def delete_user(id):
  user_ref = db.collection("users").document(id)
  user_ref.delete()
