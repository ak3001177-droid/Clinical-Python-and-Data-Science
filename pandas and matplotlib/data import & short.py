import pandas as pd

# ==========================================
# PULLING DATA FROM CSV
# ==========================================

# Yeh command tumhari CSV file ko dhoondhegi aur usko wapas DataFrame (Table) mein badal degi
imported_df = pd.read_csv("hospital_billing_report.csv")
x = imported_df.describe()
print(x)
y = imported_df["Name"]
print(y) 

print("--- Data Successfully Imported from CSV ---")
print(imported_df)

# ==========================================
# SORTING THE DATA
# ==========================================

print("\n--- VIP Patients (Highest Bill to Lowest) ---")

# Dimaag lagao: 
# 1. 'by' ke andar us column ka naam aayega jiske hisaab se sort karna hai.
# 2. ascending=False ka matlab hai bade se chhota (Descending). 

sorted_df = imported_df.sort_values(by="Total_Bill", ascending=False)

print(sorted_df)