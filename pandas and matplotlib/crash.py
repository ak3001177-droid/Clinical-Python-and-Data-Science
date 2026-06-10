import pandas as pd

# Adhura Hospital Data (None ka matlab khali jagah)
messy_data = {
    "Name": ["Ramesh", "Suresh", "Gita"],
    "Age": [None, 45, 30], 
    "Blood_Group": ["O+", None, "B+"]
}

df = pd.DataFrame(messy_data)
print("--- Adhura (Messy) Data (Notice the NaN) ---")
print(df)

# Dimaag lagao: fillna() ke brackets ke andar wo text string likho 
# jo tum 'NaN' ki jagah dikhana chahte ho (e.g., 'Unknown' ya 'Not Recorded')
clean_df = df.fillna("Unknown")

print("\n--- Saaf (Clean) Data ---")
print(clean_df)

