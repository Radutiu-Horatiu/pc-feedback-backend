from pydantic import BaseModel
from datetime import date

class User_Item(BaseModel)
    id: str
    email: str
    username: str
    name: str
    role: str
    fiscal_year: int
    personal_number: str 
    career_level: str
    organizational_assgmnt: str

class Projects_Item(BaseModel)
    project_id: str
    project_name: str
    start_date: date
    description: str

class Feedback_Item(BaseModel)
    from_user_id: str
    to_user_id : str
    status: str
    project_id: str
    anonym: bool
    list_of_categories: List[str]
    feedback_date: date

class Teams(BaseModel)
    team_id: str
    member_list: List[]
    feedback_list: List[]

class PEGS(BaseModel)
    peg_id: str
    fiscal_year: int 
    user_id: int 
    personal_number: str
    date_of_peg: date
    project_id: int
    customer_name: str
    name_of_project: str
    name_of_manager: str 
    evaluator_name: str 
    no_of_project_days_evaluated: int 
    criteria: int 
    status: str 

class PEG_Criteria(BaseModel)
    id: str
    peg_id: str 
    peg_criteria_id: str
    rating: int

class PEG_Criteria_Description(BaseModel)
    id: str
    name: str
    description: text




