import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# DATA TAIYAR KARNA
# ==========================================

# Data 1: Department Revenue (Bar Chart ke liye)
departments = ['Emergency', 'ICU', 'Surgery']
revenue = [15000, 25000, 40000]

# Data 2: ICU Patient Trend (Line Chart ke liye)
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4']
patients = [10, 15, 12, 20]

# ==========================================
# DASHBOARD BANANA (Bada Canvas set karna)
# ==========================================
# Figure size (10, 5) ka matlab Width=10 aur Height=5 hai
plt.figure(figsize=(10, 5))

# --- GRAPH 1: Left Side (Bar Chart) ---
# THE CHALLENGE 1: Screen ko 1 row aur 2 columns mein baanto, aur isko 'Pehli (1)' position par set karo.
# Hint: plt.subplot(Row, Column, Position)
plt.subplot(1, 2, 1)
plt.bar(departments, revenue, color=['red', 'blue', 'green'])
plt.title("Department Revenue (Kamai)")

# --- GRAPH 2: Right Side (Line Chart) ---
# THE CHALLENGE 2: Screen ko 1 row aur 2 columns mein hi rakhna hai, par isko 'Dusri (2)' position par set karo.
plt.subplot(1, 2, 2)
plt.plot(days, patients, marker='o', color='purple')
plt.title("ICU Patient Trend (Last 4 Days)")

# Layout ko automatically theek karne ke liye (taaki text takraye nahi)
plt.tight_layout()

# Jadoo screen par dikhana
plt.show()