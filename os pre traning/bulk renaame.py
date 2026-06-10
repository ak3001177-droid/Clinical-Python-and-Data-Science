import os

folder_path = "MRI_Scans"
prefix = "BMRIT_Scan_"

print("System: Bulk Rename protocol initiate kar rahe hain...\n")

for file_name in os.listdir(folder_path):
    # eh ward ke naam aur patient ke naam ko perfectly jod kar 
    # ek poora address (MRI_Scans/scan1.txt) bana deta hai, jise humne purana_rasta naam diya hai. Ab Python kabhi bhatkega nahi.
    purana_rasta = os.path.join(folder_path, file_name)
    
    # Step 2: Naya naam aur uska naya rasta banana
    naya_naam = prefix + file_name
    naya_rasta = os.path.join(folder_path, naya_naam)
    
    # Step 3: The Magic Weapon - Rename kar dena
    os.rename(purana_rasta, naya_rasta)
    
    print("Locked & Changed:", file_name, "-->", naya_naam)

print("\nBoss, poora dataset ek second mein format ho gaya!")