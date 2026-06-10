import pandas as pd

# Hospital Billing Data
billing_data = {
    "Name": ["Aman", "Neha", "Rohan"],
    "Room_Charge": [2000, 5000, 1500],
    "Medicine_Charge": [500, 1200, 300]
}

df = pd.DataFrame(billing_data)
print("--- Old Record ---")
print(df)

df["Total_Bill"] = df["Room_Charge"] + df["Medicine_Charge"]

print("\n--- Automated Final Bill ---")
print(df)

# Yeh command tumhare 'df' ko ek asali .csv file mein badal degi.
# index=False ka matlab hai ki wo extra 0, 1, 2 wali ginti file mein save na kare.

df.to_csv("hospital_billing_report.csv", index=False)

print("\nMISSION SUCCESS: CSV File successfully generated in your folder!")