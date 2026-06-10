import os
import shutil

source_file = "patient_report.txt"
destination_folder = "PGI_Discharged"

# Pehle radar se check karenge ki folder exist karta hai ya nahi
if os.path.exists(destination_folder):
    # The Magic Weapon: File ko copy karna
    shutil.copy(source_file, destination_folder)
    print("Boss, file ki photo-copy successfully folder mein chali gayi!")
else:
    print("Error: Destination folder toh yahan hai hi nahi!")