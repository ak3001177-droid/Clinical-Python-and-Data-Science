# Step 1: Pandas library ko apne code mein bulana (import karna)
# Hum Pandas ko chota naam 'pd' de rahe hain taaki baar-baar lamba naam na likhna pade
import pandas as pd

# Step 2: Ek chhota sa Hospital Data banana (Dictionary format mein)
patient_data = {
    "Name": ["Rahul", "Sonia", "Amit", "Priya"],
    "Age": [45, 32, 60, 28],
    "Scan_Type": ["MRI", "CT Scan", "X-Ray", "MRI"],
    "Disease": ["Tumor", "Fracture", "Normal", "Tumor"]
}

# Step 3: Pandas ka magic! Is data ko ek Dataframe (Table) mein badalna
df = pd.DataFrame(patient_data)


# Step 4: Table ko screen par print karna
print("--- Hospital Patient Records ---")
print(df)

# --- Mission 2: Filtering Data ---
print("\n--- Emergency: Tumor Patients Only ---")

# Pandas ko order diya: DataFrame (df) mein se sirf wo rows nikal ke do jahan Disease 'Tumor' ho
tumor_patients = df[df["Disease"] == "Tumor"]

print(tumor_patients)

# --- Mission 3: Medical Analytics ---
print("\n--- Hospital Daily Report ---")

# 1. Average Age nikalna (.mean() function se)
avg_age = df["Age"].mean()
print(f"Average Patient Age: {avg_age} years")

# 2. Har scan kitni baar hua, uski ginti karna (.value_counts() function se)
scan_counts = df["Scan_Type"].value_counts()
print("\nTotal Scans Done Today:")
print(scan_counts) 