import pandas as pd
import matplotlib.pyplot as plt

# 1. Initialize simulated hospital department dataset
data = {
    'Hospital_Dept': ['Radiology', 'Pathology', 'Emergency', 'Surgery'],
    'Total_Patients': [150, 200, 350, 80]
}
df = pd.DataFrame(data)

# 2. Generate Bar Chart integrating Pandas DataFrame with Matplotlib
# X-axis represents Departments, Y-axis represents Patient Count
bars = plt.bar(df['Hospital_Dept'], df['Total_Patients'], color=['purple', 'teal', 'orange', 'red'])
# Note: Single quotes ('') and double quotes ("") can be used interchangeably for strings in Python.

# 3. Advanced Annotation: Dynamically display exact numerical values atop each bar
# 'padding' creates a clean visual gap above the bar, while 'fontweight' enhances text readability.
plt.bar_label(bars, padding=3, fontweight='bold')

# 4. Plot Formatting and Aesthetics
plt.title("Hospital Patient Load (Pandas + Matplotlib)")
plt.xlabel("Departments")
plt.ylabel("Patient Count")

# 5. Render the Visualization
plt.show()