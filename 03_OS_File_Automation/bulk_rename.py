import os

# Define target directory and standardized prefix
folder_path = r"C:\Users\sujan singh\Desktop\python\03_OS_File_Automation\MRI_Scans"
#folder_path = "MRI_Scans"
prefix = "BMRIT_Scan_"

print("[SYSTEM] Initiating bulk renaming protocol...\n")

# Iterate through all files within the specified directory
for file_name in os.listdir(folder_path):
    
    # Step 1: Construct the absolute path for the existing file
    # os.path.join seamlessly merges the directory and file name to prevent path navigation errors.
    old_path = os.path.join(folder_path, file_name)
    
    # Step 2: Generate the standardized file name and its new path
    new_name = prefix + file_name
    new_path = os.path.join(folder_path, new_name)
    
    # Step 3: Execute the core file renaming operation
    os.rename(old_path, new_path)
    
    # Display real-time execution logs
    print(f"Locked & Changed: {file_name} --> {new_name}")

print("\n[SYSTEM] SUCCESS: Entire dataset has been successfully reformatted.")