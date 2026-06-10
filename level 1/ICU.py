class patient:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

ward_patient = [
    patient("Amit", 98.6),
    patient("Neha", 102.5),
    patient("RAvi", 99.1),
    patient("Pooja", 103.0),
    patient("Akhil", 101.5),
    patient("Shiva", 104.2)
]   

critical_count = 0
for p in ward_patient:
    if p.temp >= 102:
        critical_count+=1
        print(p.name, "needs attention")

print(f"total critical count:  {critical_count}")        