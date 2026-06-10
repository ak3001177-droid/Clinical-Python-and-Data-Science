import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("heart_patients.csv")
plt.scatter(df["Age"], df["Cholesterol"], color='purple')
plt.title("Age vs Cholesterol Trend")
plt.xlabel("Age")
plt.ylabel("Cholesterol")
plt.show()