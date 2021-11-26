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

def add_user(obj, uid):
  db.collection("users").document(uid).set(obj)

def update_user(id, obj):
  print(obj)
  user_ref = db.collection("users").document(id)
  try:
    user_ref.update({"name":obj["name"], "username":obj["username"]},{"email":obj["email"], "role":obj["role"]},{"fiscal year":obj["fiscal_year"], "persinal number":obj["personal_number"]},{"career level":obj["career_lever"], "organisational assigment":obj["organisational_assigment"]})
    return {"message":"updated obj"}
  except:
    return {"error":"id dosent exist"}

def delete_user(id):
  user_ref = db.collection("users").document(id)
  user_ref.delete()


def get_all_users():
  all_users=[]
  doc_ref = db.collection(u'users').stream()
  
  for user in doc_ref:
    all_users.append(user.to_dict())
  return all_users
