import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("heart_patients.csv")
staus_count = df['Status'].value_counts()
plt.bar(staus_count.index, staus_count.values, color=["red", "green", "orange"])
plt.title("Patient Risk Status")
plt.xlabel("Staus")
plt.ylabel("Counts")
plt.show()