import pandas as pd

patient_data = {
    "Name": ["Aman", "Neha", "Rohan", "Sunita", "Vikash"],
    "Age": [22, 45, 19, 52, 38],
    "Blood_Group": ["O+", "A+", "B+", "O-", "AB+"]
}

# Step 2: DataFrame Banana
df = pd.DataFrame(patient_data)

print("--- All Patients ---")
print(df)

print("\n--- Patients Above 40 Years ---")
senior_patients = df[df["Age"] > 40]

print(senior_patients)

print("\n--- High Risk Patients (Age > 40 AND Blood Group A+) ---")

high_risk = df[(df["Age"] > 40) & (df["Blood_Group"] == "A+")]
#pandas me and ka nhi balki & ka use karte hai and or ki jgh | ka use karte hai
print(high_risk)