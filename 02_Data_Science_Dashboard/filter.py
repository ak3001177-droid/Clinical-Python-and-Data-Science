import pandas as pd

# Step 1: Initialize sample patient demographic and medical data
patient_data = {
    "Name": ["Aman", "Neha", "Rohan", "Sunita", "Vikash"],
    "Age": [22, 45, 19, 52, 38],
    "Blood_Group": ["O+", "A+", "B+", "O-", "AB+"]
}

# Step 2: Convert the dictionary into a Pandas DataFrame for structured analysis
df = pd.DataFrame(patient_data)

print("--- Complete Patient Registry ---")
print(df)

# Step 3: Single-condition filtering
print("\n--- Filtered Cohort: Patients Above 40 Years ---")
senior_patients = df[df["Age"] > 40]

print(senior_patients)

# Step 4: Multi-condition filtering (Complex Logic)
print("\n--- High-Risk Cohort (Age > 40 AND Blood Group A+) ---")

# Note: In Pandas, always use bitwise operators '&' for AND, and '|' for OR 
# when combining multiple boolean conditions inside a DataFrame.
high_risk = df[(df["Age"] > 40) & (df["Blood_Group"] == "A+")]

print(high_risk)