opd_register = []
while True:
    name = input("Entere patient name or Stop: ")
    if name == "Stop":
        break
    else:
        age = int(input("Enter youre age: "))
        disease = input("Enter your disease: ")
        patient_data = {
        "name" : name,
        "age" : age,
        "disease" : disease
        }  
        opd_register.append(patient_data)
        print(f"{name}, entery is done")

print("todays total patients: ", opd_register)
