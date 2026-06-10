import datetime
current_time = str(datetime.datetime.now())
with open("hospital_log.txt", "a") as f:
    f.write(f"{current_time}, System BOOT : MRI Machine is online\n")
with open("hospital_log.txt", "r") as f:
    all_data = f.read()
    print(all_data)