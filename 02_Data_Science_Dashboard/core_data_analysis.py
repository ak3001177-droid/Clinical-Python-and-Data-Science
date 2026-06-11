import pandas as pd

# Step 1: Initialize sample hospital data (Simulating a database fetch)
patient_data = {
    "Name": ["Rahul", "Sonia", "Amit", "Priya"],
    "Age": [45, 32, 60, 28],
    "Scan_Type": ["MRI", "CT Scan", "X-Ray", "MRI"],
    "Disease": ["Tumor", "Fracture", "Normal", "Tumor"]
}

# Step 2: Convert the data dictionary into a Pandas DataFrame
df = pd.DataFrame(patient_data)

# Step 3: Display the complete patient records
print("--- Hospital Patient Records ---")
print(df)

# --- Data Filtering ---
print("\n--- Filtered Data: Tumor Diagnoses ---")

# Isolate rows where the patient's diagnosis is classified as 'Tumor'
tumor_patients = df[df["Disease"] == "Tumor"]

print(tumor_patients)

# --- Medical Analytics ---
print("\n--- Hospital Daily Analytics Report ---")

# 1. Calculate the average patient age using the .mean() function
avg_age = df["Age"].mean()
print(f"Average Patient Age: {avg_age} years")

# 2. Calculate the frequency of each scan type using the .value_counts() function
scan_counts = df["Scan_Type"].value_counts()
print("\nTotal Scans Performed Today:")
print(scan_counts)