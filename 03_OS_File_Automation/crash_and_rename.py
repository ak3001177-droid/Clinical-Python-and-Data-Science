import os

# Define the absolute base path for foolproof execution
base_path = r"C:\Users\sujan singh\Desktop\python\03_OS_File_Automation"

target_folder = os.path.join(base_path, "PGI_Patients")

print("--- PART 1: Directory Creation Protocol ---")
# Pre-execution check (Radar 1) for source creation
if os.path.exists(target_folder):
    print("[SYSTEM] Alert: Directory 'PGI_Patients' already exists. Creation bypassed.")
else:
    os.mkdir(target_folder)
    print("[SYSTEM] SUCCESS: New directory 'PGI_Patients' successfully generated.")

original_folder = os.path.join(base_path, "PGI_Patients")
renamed_folder = os.path.join(base_path, "PGI_Discharged")

print("\n--- PART 2: Directory Renaming Protocol ---")
# THE FIX: Double Radar Check (Checking both Destination and Source)

if os.path.exists(renamed_folder):
    # Failsafe: Stops the crash if 'PGI_Discharged' is already sitting there
    print("[SYSTEM] Alert: Destination directory 'PGI_Discharged' already exists! Rename operation aborted.")
    
elif os.path.exists(original_folder):
    # Failsafe: Renames ONLY if 'PGI_Patients' exists and 'PGI_Discharged' does not
    os.rename(original_folder, renamed_folder)
    print("[SYSTEM] SUCCESS: Directory successfully renamed to 'PGI_Discharged'.")
    
else:
    print("[SYSTEM] ERROR: Source directory not found. Renaming operation aborted.")