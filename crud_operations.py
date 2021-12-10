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
  user_ref = db.collection("users").document(id)
  user_ref.update({"name":obj.name, "username":obj.username, "email":obj.email, "role":obj.role, "fiscal_year":obj.fiscal_year, "personal_number":obj.personal_number,"career_level":obj.career_level, "organisational_assigment":obj.organisational_assigment})
  return {"message":"updated obj"}

def delete_user(id):
  user_ref = db.collection("users").document(id)
  user_ref.delete()

def add_feedback(obj):
  db.collection("feedback").document(obj["uid"]).set(obj)

#add_feedback({"nume": "inca un test", "prenume": "test9999"})

def get_feedback(id_feedback):
  feedback_ref = db.collection("feedback").document(id_feedback)
  return feedback_ref.get().to_dict()

print(get_feedback("rd17sULU01bO4WieLFdP"))

def update_feedback(feedback_id, obj):
    print(obj)
    feedback_ref = db.collection("feedback").document(feedback_id)
    feedback_ref.update(obj)
    try:
      feedback_ref.update({"from_user_id": obj["from_user_id"], "to_user_id": obj["to_user_id"]}, {"status": obj["status"], "project_id": obj["project_id"]},
                      {"anonym": obj["anonym"], "list_of_categories": obj["list_of_categories"]},
                      {"feedback_date": obj["feedback_date"],
                       "organisational assigment": obj["organisational_assigment"]})
      return {"message": "updated obj"}
    except:
      return {"error": "id dosent exist"}

#update_feedback("rd17sULU01bO4WieLFdP",{"nume": "test2", "prenume": "test234"})


def delete_feedback(id_feedback):
  feedback_ref = db.collection("feedback").document(id_feedback)
  feedback_ref.delete()

#delete_feedback("KF6rs09M1yLkrk4ZLHT3")
