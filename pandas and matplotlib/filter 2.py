import pandas as pd
import matplotlib.pyplot as plt

# 1. Hospital ka raw data (Database se nikala hua)
data = {
    'Patient_Name': ['Rahul', 'Aman', 'Priya', 'Suresh', 'Neha', 'Rohan'],
    'Department': ['Radiology', 'Emergency', 'Surgery', 'Emergency', 'Pathology', 'Emergency'],
    'Bill_Amount': [5000, 12000, 45000, 8000, 2000, 15000]
}
df = pd.DataFrame(data)

# 2. THE CHALLENGE: Yahan tumhe filter lagana hai taaki sirf 'Emergency' department wale patients bachein
# Dimaag lagao aur Hint 1 ka use karke is line ko poora karo:
emergency_data = df[df['Department'] == 'Emergency']

# 3. Bar Chart banana (Ab 'df' ki jagah hum 'emergency_data' ka use karenge kyunki wo filter ho chuka hai)
plt.bar(emergency_data['Patient_Name'], emergency_data['Bill_Amount'], color=['red', 'orange', 'yellow'])
plt.title("Emergency Department - Patient Bills")
plt.xlabel("Patient Names")
plt.ylabel("Bill Amount (INR)")

# 4. THE CHALLENGE: Graph ko 'emergency_report.png' naam se apne computer mein save karo
# Hint 2 ka use karo:
plt.savefig('emergency_report.png')

# 5. Screen par dikhana
plt.show()