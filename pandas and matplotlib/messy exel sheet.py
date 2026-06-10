import pandas as pd
dirty_data = {
    'Patient_ID': [101, 102, 103, 104, 105],
    'Name': ['Rahul', 'Aman', 'Priya', 'Neha', 'Rohan'],
    'Age': [45, None, 50, 28, None], 
    'Bill_Amount': [5000, 12000, None, 8000, 15000] 
}
# Yahan isko DataFrame (df) mein convert karo

df = pd.DataFrame(dirty_data)
print(df.isnull().sum()) #(Yeh command tumhe bata dega ki Age mein kitne blanks hain aur Bill mein kitne).
df["Age"] = df['Age'].fillna(0)
df["Bill_Amount"] = df['Bill_Amount'].fillna(0) 
print(df)