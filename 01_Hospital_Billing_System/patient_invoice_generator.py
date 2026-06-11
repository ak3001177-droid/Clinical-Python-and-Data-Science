patient_1 = {
    "Name" : "Suresh",
    "Age" : 65,
    "Test" : "MRI Scan",
    "Bill" : 8000
}

patient_2 = {
    "Name" : "Divyansh",
    "Age" : 25,
    "Test" : "X-Ray",
    "Bill" : 2000
}

def generate_bill(data):
    if data["Age"] >= 60:
        data["Bill"] = data["Bill"] - 1000
        
    print(data["Name"], "ka final Bill", data["Bill"],".RS hai")


generate_bill(patient_1)
generate_bill(patient_2)     
         


