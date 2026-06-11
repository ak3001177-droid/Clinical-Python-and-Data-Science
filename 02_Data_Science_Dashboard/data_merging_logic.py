import pandas as pd
df1 = pd.read_csv('health_data.csv')
df2 = pd.read_csv('hospital_status.csv')
avg_age = df1['Age'].mean()
df1["Age"] = df1["Age"].fillna(avg_age)
master_df = pd.merge(df1, df2, on='Patient_ID')
master_df["BMI"] = master_df["Weight_kg"] / (master_df["Height_m"] * master_df["Height_m"])
icu_patients = master_df[master_df['Department'] == 'ICU']
icu_patients.to_csv('final_icu_report.csv', index=False)
