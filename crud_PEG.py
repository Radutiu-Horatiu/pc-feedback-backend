from models import PEG_Item
from typing import List
from firebase import db
import datetime
import time

def add_peg(obj):
    peg_obj = {
        "Fiscal year": obj.fiscal_year,
        "User id": obj.user_id,
        "Date of PEG": obj.date_of_peg,
        "Project id": obj.project_id,
        "Customer name": obj.customer_name,
        "Project name": obj.name_of_project,
        "Manager name": obj.name_of_manager,
        "Evaluator name": obj.evaluator_name,
        "Number of project days evaluated": obj.no_of_project_days_evaluated,
        "Criteria": obj.criteria,
        "Status": obj.status
    }
    db.collection("peg").add(peg_obj)

def get_all_pegs():
  allPegs = []
  pegs = db.collection(u'peg').stream()
  for peg in pegs:
      my_peg = peg.to_dict()
      my_peg["id"] = peg.id
      allPegs.append(my_peg)    
  return allPegs

def get_peg(id):
    peg_ref = db.collection(u'peg').document(id)
    return peg_ref.get().to_dict()


def delete_peg(id):
  peg_ref = db.collection("peg").document(id)
  peg_ref.delete() 

