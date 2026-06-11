import pandas as pd
import matplotlib.pyplot as plt

# --- DATA INITIALIZATION ---

# Dataset 1: Departmental Revenue Analytics (For Bar Chart)
departments = ['Emergency', 'ICU', 'Surgery']
revenue = [15000, 25000, 40000]

# Dataset 2: ICU Patient Admission Trends (For Line Chart)
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4']
patients = [10, 15, 12, 20]

# --- DASHBOARD CONFIGURATION (Canvas Setup) ---

# Initialize the master figure canvas with specific dimensions (Width=10, Height=5)
plt.figure(figsize=(10, 5))

# --- SUBPLOT 1: Left Panel (Bar Chart) ---
# Syntax: plt.subplot(Rows, Columns, Index Position)
# Configures a 1x2 grid structure, assigning this specific chart to position 1.
plt.subplot(1, 2, 1)
plt.bar(departments, revenue, color=['red', 'blue', 'green'])
plt.title("Department Revenue")

# --- SUBPLOT 2: Right Panel (Line Chart) ---
# Utilizing the same 1x2 grid structure, assigning this line chart to position 2.
plt.subplot(1, 2, 2)
plt.plot(days, patients, marker='o', color='purple')
plt.title("ICU Patient Trend (Last 4 Days)")

# Optimizes the spacing between subplots to prevent overlapping text and labels
plt.tight_layout()

# Render the complete multi-chart dashboard on the screen
plt.show()