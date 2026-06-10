import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# MISSION 1: THE DATA MERGER (Files ko Jodna)
# ==========================================

# File 1: Reception ka data (Patient ki details)
reception_data = {
    'Patient_ID': [101, 102, 103],
    'Name': ['Aman', 'Priya', 'Rohan'],
    'Age': [45, 30, 50]
}
df_reception = pd.DataFrame(reception_data)

# File 2: Billing department ka data (Patient ka bill)
billing_data = {
    'Patient_ID': [101, 102, 103],
    'Department': ['ICU', 'Radiology', 'Surgery'],
    'Bill_Amount': [50000, 5000, 80000]
}
df_billing = pd.DataFrame(billing_data)

# THE CHALLENGE 1: In dono files ko 'Patient_ID' ke zariye aapas mein jodo.
# Hint: pd.merge(Pehli_File, Dusri_File, on='Common_Column_Ka_Naam')
master_table = pd.merge(df_reception, df_billing, on='Patient_ID') 

# Screen par judne ke baad ka jadoo dekhna:
print("Master Table Ban Gayi:\n")
print(master_table)
print("\n" + "="*40 + "\n")


# ==========================================
# MISSION 2: THE TREND TRACKER (Line Chart)
# ==========================================

# Data: Pichle 5 din mein ICU aane wale patients
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
icu_patients = [5, 8, 12, 7, 15]

# THE CHALLENGE 2: In numbers ka ek Line Chart banao taaki trend dikhe.
# Hint: plt.plot(x_axis_data, y_axis_data, marker='o', color='red')
plt.plot(days, icu_patients, marker='o', color='red')

# Chart ki Formatting
plt.title("ICU Patient Trend (Last 5 Days)")
plt.xlabel("Days")
plt.ylabel("Number of Patients")
plt.grid(True) # Isse graph ke piche lines aa jayengi taaki padhna aasan ho
plt.show()