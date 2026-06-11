import pandas as pd

# 1. Initialize the core hospital billing dataset
billing_data = {
    "Name": ["Aman", "Neha", "Rohan"],
    "Room_Charge": [2000, 5000, 1500],
    "Medicine_Charge": [500, 1200, 300]
}

df = pd.DataFrame(billing_data)
print("--- Initial Billing Records (Raw Data) ---")
print(df)

# 2. Automated Feature Engineering: Calculate the total bill dynamically
df["Total_Bill"] = df["Room_Charge"] + df["Medicine_Charge"]

print("\n--- Finalized Automated Billing Statement ---")
print(df)

# 3. Data Export Pipeline
# Export the structured DataFrame to an external CSV file.
# Note: 'index=False' ensures that the auto-generated Pandas indices are excluded from the final report.
df.to_csv("hospital_billing_report.csv", index=False)

print("\n[SYSTEM] SUCCESS: hospital_billing_report.csv has been successfully generated in the local directory.")