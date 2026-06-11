import os

# 1. Environment Awareness: Retrieve and display the Current Working Directory (CWD)
print(f"[SYSTEM] Current Execution Path: {os.getcwd()}")

# 2. Directory Audit: Scan and list all contents within the current path
print(f"[SYSTEM] Directory Contents Audit: {os.listdir()}")

# 3. Workspace Initialization: Create a new directory
folder_name = "temporary_workspace"
os.mkdir(folder_name)
print(f"[SYSTEM] SUCCESS: Directory '{folder_name}' securely generated.")

# 4. Workspace Cleanup: Remove the specified directory
# Failsafe Note: os.rmdir() strictly targets and deletes only empty directories.
os.rmdir(folder_name)
print(f"[SYSTEM] SUCCESS: Directory '{folder_name}' has been completely purged.")