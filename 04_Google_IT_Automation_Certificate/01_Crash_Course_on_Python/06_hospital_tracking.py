# MEDICAL MEGA PROJECT: Hospital Patient Tracking System

def get_event_date(event):
    # Function to return the date associated with the event
    return event.date

def current_patients(events):
    # 1. First, sort all events chronologically based on their time
    events.sort(key=get_event_date)
    
    # 2. Create an empty register (Dictionary)
    wards = {}
    
    # 3. Check each event one by one
    for event in events:
        # If the Ward name is not in the register, create a new empty set
        if event.ward not in wards:
            wards[event.ward] = set()
            
        # If the patient is ADMITTED, add them to the ward's set
        if event.type == "admit":
            wards[event.ward].add(event.patient)
            
        # If the patient is DISCHARGED, first check if they are in the ward, then remove them
        elif event.type == "discharge":
            if event.patient in wards[event.ward]: # Safety Check!
                wards[event.ward].remove(event.patient)
                
    return wards

def generate_report(wards):
    print("\n🏥 CURRENT HOSPITAL ADMISSION REPORT 🏥")
    print("-" * 40)
    for ward, patients in wards.items():
        # Only print the ward if there is at least 1 patient currently admitted
        if len(patients) > 0:
            patient_list = ", ".join(patients)
            print("{}: {}".format(ward, patient_list))
    print("-" * 40)


# Object-Oriented Programming

class PatientEvent:
    def __init__(self, event_date, event_type, ward_name, patient_name):
        self.date = event_date
        self.type = event_type
        self.ward = ward_name
        self.patient = patient_name


# THE DATA (System Logs)

events = [
    PatientEvent('2026-06-25 08:00', 'admit', 'ICU', 'Aarav'),
    PatientEvent('2026-06-25 09:30', 'admit', 'General Ward', 'Neha'),
    PatientEvent('2026-06-25 10:15', 'admit', 'ICU', 'Vikram'),
    PatientEvent('2026-06-25 12:00', 'discharge', 'ICU', 'Aarav'), # Aarav is discharged
    PatientEvent('2026-06-25 14:00', 'admit', 'Radiology Dept', 'Suresh'),
    PatientEvent('2026-06-25 15:30', 'discharge', 'General Ward', 'Rahul') # Error check: Rahul was never admitted!
]


# RUN THE SCRIPT

active_wards = current_patients(events)
generate_report(active_wards)