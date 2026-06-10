import datetime
def admit_to_vailt(name, scan):
    current_time = str(datetime.datetime.now())
    patient_data = {
        "name" : name,
        "Scan_type" : scan,
        "Time" : current_time
    }
    try:
        with open("master_log.txt", "a") as f:
            f.write(str(patient_data) + "\n")
    except Exception:
        print("Vault Error!")

admit_to_vailt("Gemini", "MRI")                           