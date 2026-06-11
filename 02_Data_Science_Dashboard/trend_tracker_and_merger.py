import pandas as pd
import matplotlib.pyplot as plt

# --- DATA INTEGRATION (Dataset Merging) ---

# Dataset 1: Reception Desk Records (Patient Demographics)
reception_data = {
    'Patient_ID': [101, 102, 103],
    'Name': ['Aman', 'Priya', 'Rohan'],
    'Age': [45, 30, 50]
}
df_reception = pd.DataFrame(reception_data)

# Dataset 2: Billing Department Records (Financial Data)
billing_data = {
    'Patient_ID': [101, 102, 103],
    'Department': ['ICU', 'Radiology', 'Surgery'],
    'Bill_Amount': [50000, 5000, 80000]
}
df_billing = pd.DataFrame(billing_data)

# Merge both DataFrames using 'Patient_ID' as the primary key.
# Syntax: pd.merge(DataFrame1, DataFrame2, on='Common_Column')
master_table = pd.merge(df_reception, df_billing, on='Patient_ID') 

# Display the consolidated master table
print("--- Consolidated Master Table ---\n")
print(master_table)
print("\n" + "="*40 + "\n")

# --- TREND ANALYSIS (Line Chart Visualization) ---

# Dataset: ICU patient admissions over the last 5 days
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
icu_patients = [5, 8, 12, 7, 15]

# Generate a Line Chart to visualize the admission trend.
# Syntax: plt.plot(x_axis_data, y_axis_data, marker='o', color='red')
plt.plot(days, icu_patients, marker='o', color='red')

# Apply professional formatting and aesthetics
plt.title("ICU Patient Trend (Last 5 Days)")
plt.xlabel("Days")
plt.ylabel("Number of Patients")
plt.grid(True) # Enables gridlines for better readability and precision

# Render the visualization on screen
plt.show()