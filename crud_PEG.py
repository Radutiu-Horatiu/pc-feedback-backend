from models import PEG_Item
from firebase import db
import datetime
import time

def add_peg(obj):
    date_of_peg = obj.date_of_peg.strftime("%m-%d-%Y")
    date = datetime.datetime.strptime(date_of_peg, "%m-%d-%Y")
    time_tuple = date.timetuple()
    timestamp = time.mktime(time_tuple)
    peg_obj = {
        "Fiscal year": obj.fiscal_year,
        "User id": obj.user_id,
        "Personal Number": obj.personal_number,
        "Date of PEG": timestamp,
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

