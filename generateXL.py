import xlsxwriter
from firebase import db
from xlsxwriter import worksheet, workbook
from crud_PEG import get_peg
from crud_operations import get_user
from models import PEG_Item
from models import User_Item



def complete_PEG(id: str):


        workbook = xlsxwriter.Workbook('PEGS.xlsx')
        worksheet = workbook.add_worksheet("Requested PEG")
        dict = get_peg(id)

        worksheet.set_column('A:A', 30)
        worksheet.set_column('B:B', 30)
        worksheet.set_column('C:C', 30)
        worksheet.set_column('D:D', 30)
        worksheet.write(0, 0, "Fiscal Year")
        worksheet.write(1, 0, "Employee Name")
        worksheet.write(2, 0, "Personnel Number")
        worksheet.write(3, 0, "Current career level")
        worksheet.write(4, 0, "Organizational Assignment")
        worksheet.write(5, 0, "Date of PEG")
        worksheet.write(6, 0, "Project ID")
        worksheet.write(7, 0, "Customer Name")
        worksheet.write(8, 0, "Name of the Project")
        worksheet.write(9, 0, "Name of the Project Manager")
        worksheet.write(10, 0, "Name of the Evaluator")
        worksheet.write(11, 0, "Number of project days evaluated")

        worksheet.write(13, 0, "Criteria")
        worksheet.write(13, 1, "Rating")
        worksheet.write(13, 2, "Description of the rating")
        worksheet.write(13, 3, "Recommandations / Comments")

        worksheet.write(14, 0, "Professional and industry Experience")
        worksheet.write(15, 0, "Project and program Management")
        worksheet.write(16, 0, "Strategy focus")
        worksheet.write(17, 0, "Customer focus")
        worksheet.write(18, 0, "Employee focus")
        worksheet.write(19, 0, "Focus on excellence")
        worksheet.write(20, 0, "Overall Rating")

        average=0



        worksheet.write(0, 1, dict["Fiscal year"])

        worksheet.write(2, 1, dict["User id"])
        user=get_user(dict["User id"])

        worksheet.write(1, 1, user["name"])
        worksheet.write(3, 1, user["career_level"])
        worksheet.write(4, 1, user["organisational_assignment"])

        worksheet.write(5, 1, dict["Date of PEG"])
        worksheet.write(6, 1, dict["Project id"])
        worksheet.write(7, 1, dict["Customer name"])
        worksheet.write(8, 1, dict["Project name"])
        worksheet.write(9, 1, dict["Manager name"])
        worksheet.write(10, 1, dict["Evaluator name"])
        worksheet.write(11, 1, dict["Number of project days evaluated"])

        worksheet.write(14, 1, dict["result"]["prof_industry_exp"]["rating"])
        worksheet.write(14, 2, dict["result"]["prof_industry_exp"]["description"])
        worksheet.write(14, 3, dict["result"]["prof_industry_exp"]["comments"])
        average+=dict["result"]["prof_industry_exp"]["rating"]

        worksheet.write(15, 1, dict["result"]["proj_program_management"]["rating"])
        worksheet.write(15, 2, dict["result"]["proj_program_management"]["description"])
        worksheet.write(15, 3, dict["result"]["proj_program_management"]["comments"])
        average+=dict["result"]["proj_program_management"]["rating"]

        worksheet.write(16, 1, dict["result"]["strategy_focus"]["rating"])
        worksheet.write(16, 2, dict["result"]["strategy_focus"]["description"])
        worksheet.write(16, 3, dict["result"]["strategy_focus"]["comments"])
        average+=dict["result"]["strategy_focus"]["rating"]

        worksheet.write(17, 1, dict["result"]["customer_focus"]["rating"])
        worksheet.write(17, 2, dict["result"]["customer_focus"]["description"])
        worksheet.write(17, 3, dict["result"]["customer_focus"]["comments"])
        average+=dict["result"]["customer_focus"]["rating"]

        worksheet.write(18, 1, dict["result"]["employee_focus"]["rating"])
        worksheet.write(18, 2, dict["result"]["employee_focus"]["description"])
        worksheet.write(18, 3, dict["result"]["employee_focus"]["comments"])
        average+=dict["result"]["employee_focus"]["rating"]

        worksheet.write(19, 1, dict["result"]["excellence_focus"]["rating"])
        worksheet.write(19, 2, dict["result"]["excellence_focus"]["description"])
        worksheet.write(19, 3, dict["result"]["excellence_focus"]["comments"])
        average+=dict["result"]["excellence_focus"]["rating"]
        average/=6.00


        worksheet.write(20,1,average)

        workbook.close()



    #complete_PEG("vub1vtrOSez9TtqwlRgf")