# Step 1: Initialize file creation and write operations ('w' mode)
with open("patient_log.txt", "w") as file:
    file.write("PGI Lucknow - BMRIT Department\n")
    file.write("Patient 01: MRI Scan completed successfully.\n")

print("[SYSTEM] SUCCESS: Background file generation and data writing completed.")

# Step 2: Read data from the file ('r' mode)
# The 'with' context manager automatically ensures the file is safely closed after execution.
with open("patient_log.txt", "r") as f:
    # f.read() extracts the entire contents of the file into memory
    all_data = f.read()

print("--- Retrieved File Data ---\n")
print(all_data)
print("\n[SYSTEM] SUCCESS: Data extraction completed successfully.")