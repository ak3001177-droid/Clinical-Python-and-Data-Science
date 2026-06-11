import pandas as pd
dirty_data = {
    'Patient_ID': [101, 102, 103, 104, 105],
    'Name': ['Rahul', 'Aman', 'Priya', 'Neha', 'Rohan'],
    'Age': [45, None, 50, 28, None], 
    'Bill_Amount': [5000, 12000, None, 8000, 15000] 
}

df = pd.DataFrame(dirty_data)
avg_age = df['Age'].mean()
df["Age"] = df['Age'].fillna(avg_age)
df = df.dropna()  #it will remove any remaining rows with missing values
print(df)
df.to_csv("clean_hospital_data.csv", index=False)