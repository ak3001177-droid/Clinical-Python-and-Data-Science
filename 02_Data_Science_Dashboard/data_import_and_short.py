import pandas as pd

# --- DATA IMPORT & EXPLORATION ---
csv_path = r"C:\Users\sujan singh\Desktop\python\02_Data_Science_Dashboard\hospital_billing_report.csv"

# Load the external CSV file into a Pandas DataFrame for analysis
imported_df = pd.read_csv(csv_path)

# Generate and display a statistical summary of the dataset
x = imported_df.describe()
print(x)

# Extract and isolate the patient 'Name' column
y = imported_df["Name"]
print(y) 

print("--- Dataset Successfully Loaded from CSV ---")
print(imported_df)

# --- DATA SORTING & PRIORITIZATION ---

print("\n--- High-Value Patient Accounts (Descending Order) ---")

# Sort the DataFrame based on the 'Total_Bill' column
# Setting 'ascending=False' sorts the records from highest to lowest bill amount
sorted_df = imported_df.sort_values(by="Total_Bill", ascending=False)

print(sorted_df)