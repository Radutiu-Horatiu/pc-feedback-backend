from pydantic import BaseModel
from datetime import date
from typing import List


class User_Item(BaseModel):
    id: str
    email: str
    username: str
    name: str
    role: str
    fiscal_year: int
    personal_number: str 
    career_level: str
    organizational_assgmnt: str

class Projects_Item(BaseModel):
    project_id: str
    project_name: str
    start_date: date
    description: str

class Feedback_Item(BaseModel):
    from_user_id: str
    to_user_id : str
    status: str
    project_id: str
    anonym: bool
    category: str
    text: str

class Team_Item(BaseModel):
    team_id: str
    member_list: List[User_Item]
    feedback_list: List[Feedback_Item]

class PEG_Item(BaseModel):
    peg_id: str
    fiscal_year: int 
    user_id: str
    date_of_peg: str
    project_id: str
    customer_name: str
    name_of_project: str
    name_of_manager: str 
    evaluator_name: str 
    no_of_project_days_evaluated: int 
    criteria: int 
    status: str

class PEG_Result_Criteria(BaseModel):
    name: str
    rating: int
    description: str
    comments: str

class PEG_Result(BaseModel):
    peg_id: str
    prof_industry_exp: PEG_Result_Criteria
    proj_program_management: PEG_Result_Criteria
    strategy_focus: PEG_Result_Criteria
    customer_focus: PEG_Result_Criteria
    employee_focus: PEG_Result_Criteria
    excellence_focus: PEG_Result_Criteria
    overall_rating: float

class PEG_Criteria_Item(BaseModel):
    peg_criteria_id: str
    peg_id: str 
    rating: int

class PEG_Criteria_Description_Item(BaseModel):
    id: str
    name: str
    description: str





