import pandas as pd
import matplotlib.pyplot as plt

# 1. Initialize raw hospital billing dataset
data = {
    'Patient_Name': ['Rahul', 'Aman', 'Priya', 'Suresh', 'Neha', 'Rohan'],
    'Department': ['Radiology', 'Emergency', 'Surgery', 'Emergency', 'Radiology', 'Surgery'],
    'Bill_Amount': [5000, 12000, 45000, 8000, 7000, 55000]
}
df = pd.DataFrame(data)

# 2. Data Aggregation: Calculate total revenue per department
# Syntax: df.groupby('Category_Column')['Target_Value_Column'].sum()
dept_revenue = df.groupby('Department')['Bill_Amount'].sum()

# 3. Data Visualization: Generate a Pie Chart from the aggregated revenue data
# The 'autopct' parameter automatically calculates and formats the percentage for each slice.
plt.pie(dept_revenue, labels=dept_revenue.index, autopct='%1.1f%%', colors=['red', 'blue', 'orange'])

# 4. Plot Formatting and Rendering
plt.title("Hospital Revenue by Department")
plt.show()