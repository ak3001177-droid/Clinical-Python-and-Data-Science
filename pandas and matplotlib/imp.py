import pandas as pd
import matplotlib.pyplot as plt

dirty_hospital_data = {
    'Patient_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Department': ['ICU', 'Emergency', 'ICU', 'Surgery', 'Emergency', 'Surgery', 'ICU', 'Emergency'],
    'Age': [45, 22, None, 50, 34, None, 60, 25],
    'Bill_Amount': [50000, 15000, 45000, None, 12000, 80000, 55000, 10000]
}
df = pd.DataFrame(dirty_hospital_data)
avg_age = df['Age'].mean()
df["Age"] = df["Age"].fillna(avg_age)
df = df.dropna(subset=["Bill_Amount"])
dep_revenue = df.groupby('Department')['Bill_Amount'].sum()
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.bar(dep_revenue.index, dep_revenue.values,color = ["red", "blue", "green"])
plt.title("Deprtment revenue")

plt.subplot(1, 2, 2)
plt.hist(df['Age'], bins=4, color = ["orange"], edgecolor = ["black"])
df.to_csv("final_audit_report.csv", index=False)
plt.show() 

