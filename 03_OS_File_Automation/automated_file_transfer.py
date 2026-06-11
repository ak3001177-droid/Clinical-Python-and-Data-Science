import os
import shutil

#source_file = "patient_report.txt"
#destination_folder = "PGI_Discharged"

source_file = r"C:\Users\sujan singh\Desktop\python\03_OS_File_Automation\patient_report.txt"
destination_folder = r"C:\Users\sujan singh\Desktop\python\03_OS_File_Automation\PGI_Discharged"

# Pre-execution Check: Verify if the destination directory exists
if os.path.exists(destination_folder):
    # Execute File Duplication: Copy the source file to the destination directory
    shutil.copy(source_file, destination_folder)
    print("[SYSTEM] SUCCESS: File successfully copied to the destination folder.")
else:
    print("[SYSTEM] ERROR: Destination directory not found. Aborting operation.")