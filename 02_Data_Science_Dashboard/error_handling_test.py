import pandas as pd

# 1. Initialize an incomplete hospital dataset (Simulating missing records with 'None')
messy_data = {
    "Name": ["Ramesh", "Suresh", "Gita"],
    "Age": [None, 45, 30], 
    "Blood_Group": ["O+", None, "B+"]
}

df = pd.DataFrame(messy_data)
print("--- Raw/Incomplete Dataset (Note the NaN values) ---")
print(df)

# 2. Data Imputation: Handling Missing Values
# The fillna() function replaces all 'NaN' (Not a Number) entries 
# with a standardized string (e.g., 'Unknown' or 'Not Recorded') to prevent calculation errors.
clean_df = df.fillna("Unknown")

print("\n--- Cleaned/Imputed Dataset ---")
print(clean_df)