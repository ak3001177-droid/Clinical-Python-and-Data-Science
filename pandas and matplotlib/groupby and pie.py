import pandas as pd
import matplotlib.pyplot as plt

# 1. Hospital ka raw billing data
data = {
    'Patient_Name': ['Rahul', 'Aman', 'Priya', 'Suresh', 'Neha', 'Rohan'],
    'Department': ['Radiology', 'Emergency', 'Surgery', 'Emergency', 'Radiology', 'Surgery'],
    'Bill_Amount': [5000, 12000, 45000, 8000, 7000, 55000]
}
df = pd.DataFrame(data)

# 2. THE CHALLENGE 1 (Grouping): Har department ka total bill jodo
# Hint 1: groupby('Jis_Column_Ka_Group_Banana_Hai')['Jis_Column_Ko_Jodna_Hai'].sum()
dept_revenue = df.groupby('Department')['Bill_Amount'].sum()

# 3. THE CHALLENGE 2 (Pie Chart): Group kiye hue data ka Pie Chart banao
# Hint 2: plt.pie(Data_ka_naam, labels=Data_ka_naam.index, autopct='%1.1f%%')
plt.pie(dept_revenue, labels=dept_revenue.index, autopct='%1.1f%%', colors=['red', 'blue', 'orange'])

# 4. Chart ko title dena aur dikhana
plt.title("Hospital Revenue by Department")
plt.show()