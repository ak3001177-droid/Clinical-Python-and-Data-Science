# Step 1: File ko "w" (Write) mode mein kholna
with open("patient_log.txt", "w") as file:
    file.write("PGI Lucknow - BMRIT Department\n")
    file.write("Patient 01: MRI Scan completed successfully.\n")

print("Boss, background mein file ban bhi gayi aur usme data likh bhi diya!")

# 'with open as' block automatically file ko close kar deta hai, toh hum manually close karne ki zarurat nahi hai.
with open("patient_log.txt", "r") as f:
    # file.read() sara data ek hi baar mein utha laata hai
    saara_data = f.read()

print("File ke andar yeh likha hai:\n")
print(saara_data)
print("\nBoss, Data successfully read kar liya gaya hai!")