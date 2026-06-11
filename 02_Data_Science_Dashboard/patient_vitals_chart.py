import matplotlib.pyplot as plt

# 1. Initialize simulated dataset for hospital equipment usage
machines = ['X-Ray', 'CT Scan', 'MRI', 'PET']
patients = [45, 20, 15, 5]

# 2. Generate the Bar Chart with specific color encodings
# Parameters passed in order: X-axis categories, Y-axis values, and custom colors.
plt.bar(machines, patients, color=['red', 'blue', 'green', 'orange'])

# 3. Apply professional formatting: Title and axis labels
plt.title("Daily Patient Scans (Mock Data)")
plt.xlabel("Equipment Type")
plt.ylabel("Number of Patients")

# 4. Render the visualization on the screen (Crucial for final output)
plt.show()