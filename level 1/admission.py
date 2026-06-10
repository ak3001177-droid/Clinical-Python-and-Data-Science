class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
        self.bill = 0
    def admit_patient(self):
        if(self.disease == "Heart Disease" or self.age > 60):
            self.bill = 5000
            print(f"{self.name} is admitted with {self.disease}. and admitted to ICU ward. Total Bill: Rs.{self.bill}")
        else:
            self.bill = 1000
            print(f"{self.name} is admitted with {self.disease}.and admitted to general ward. Total Bill: Rs.{self.bill}")  

tody_patient = [
    Patient("Suresh", 65, "Fever"),
    Patient("Amit", 25, "Heart Disease"),
    Patient("Neha", 30, "Cough")
]      

for patient in tody_patient:
    patient.admit_patient()
            