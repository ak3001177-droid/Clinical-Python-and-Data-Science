import pandas as pd

# 1. Initialize a dataset containing missing values (simulating raw hospital records)
dirty_data = {
    'Patient_ID': [101, 102, 103, 104, 105],
    'Name': ['Rahul', 'Aman', 'Priya', 'Neha', 'Rohan'],
    'Age': [45, None, 50, 28, None], 
    'Bill_Amount': [5000, 12000, None, 8000, 15000] 
}

# 2. Convert the raw dictionary into a structured Pandas DataFrame
df = pd.DataFrame(dirty_data)

# 3. Data Audit: Calculate and display the exact count of missing (null) values per column
print("--- Null Values Diagnostic Report ---")
print(df.isnull().sum()) 

# 4. Data Imputation: Replace all missing values (NaN) with 0 to prevent calculation errors
df["Age"] = df['Age'].fillna(0)
df["Bill_Amount"] = df['Bill_Amount'].fillna(0) 

# 5. Display the finalized, cleaned dataset
print("\n--- Cleaned Patient Dataset (Post-Imputation) ---")
print(df)