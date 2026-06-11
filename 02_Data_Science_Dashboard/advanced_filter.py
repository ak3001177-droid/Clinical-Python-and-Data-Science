import pandas as pd
import matplotlib.pyplot as plt

# 1. Initialize raw hospital dataset (Simulated database extraction)
data = {
    'Patient_Name': ['Rahul', 'Aman', 'Priya', 'Suresh', 'Neha', 'Rohan'],
    'Department': ['Radiology', 'Emergency', 'Surgery', 'Emergency', 'Pathology', 'Emergency'],
    'Bill_Amount': [5000, 12000, 45000, 8000, 2000, 15000]
}
df = pd.DataFrame(data)

# 2. Filter dataset to isolate 'Emergency' department patients
emergency_data = df[df['Department'] == 'Emergency']

# 3. Generate a bar chart using the filtered 'Emergency' dataset
plt.bar(emergency_data['Patient_Name'], emergency_data['Bill_Amount'], color=['red', 'orange', 'yellow'])
plt.title("Emergency Department - Patient Bills")
plt.xlabel("Patient Names")
plt.ylabel("Bill Amount (INR)")

# 4. Export and save the generated visualization locally
plt.savefig('emergency_report.png')

# 5. Render the plot on screen
plt.show()