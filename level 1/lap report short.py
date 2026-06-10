lab_reports = {
    "REP_101" : {"Name": "Aman", "Dept": "Pathology", "Condition": "Critical"
                 },
    "REP_102" : {"Name": "Ravi", "Dept": "Radiology", "Condition": "Normal"
                 },
    "REP_103" : {"Name": "Suman", "Dept": "Cardiology", "Condition": "Critical"
                 },
    "REP_104" : {"Name": "Vikas", "Dept": "Pathology", "Condition": "Normal"
                 }
}

urgent_action = []

regular_check = []
for pet in lab_reports:
    if  lab_reports[pet]["Condition"] == "Critical":
        urgent_action.append(lab_reports[pet]["Name"] + "---"+ lab_reports[pet]["Dept"])
    else:
        regular_check.append(lab_reports[pet]["Name"] + "---"+ lab_reports[pet]["Dept"]) 

print("HOD Sir, Urgent Attention Required:", urgent_action)

print("Regular Reports:", regular_check) 