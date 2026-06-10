class Mri_machine:
    def __init__(self, machine_name):
        self.name = machine_name
        self.status = "OFF"
    def stat_scan(self):
        self.status = "RUNNING"
        print(f"{self.name} is now {self.status} Scanning patient...")


scanner_1 = Mri_machine("Siemens 3T")
scanner_1.stat_scan()