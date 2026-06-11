class OPDPatient:
    def __init__(self, name, age, his_insaurance):
        self.name = name
        self.age = age
        self.his_ins = his_insaurance
        self.bill = 500

    def finalbill(self):
        if self.his_ins == True:
            self.bill = 0
        elif(self.age > 60):
            self.bill = self.bill - 200 
        elif(self.age < 12):
            self.bill = self.bill - 300

today_patient = [
    OPDPatient("Ramesh", 65, False),
    OPDPatient("Sita", 45, True),
    OPDPatient("Vikrum", 30, False),
    OPDPatient("Shiva", 10, False)
]  

for p in today_patient:
    p.finalbill()
    print(p.name, "-", p.bill)     