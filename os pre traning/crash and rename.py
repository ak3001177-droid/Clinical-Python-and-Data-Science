import os

folder_name = "PGI_Patients"

# Radar se check kar rahe hain
if os.path.exists(folder_name):
    print("Boss, crash hone se bacha liya! Yeh folder pehle se yahan maujood hai.")
else:
    os.mkdir(folder_name)
    print("Naya folder successfully ban gaya!")

purana_naam = "PGI_Patients"
naya_naam = "PGI_Discharged"

# Radar check (taaki crash na ho)
if os.path.exists(purana_naam):
    os.rename(purana_naam, naya_naam)
    print("Naam successfully badal gaya boss!")
else:
    print("Purana folder toh mil hi nahi raha!")    