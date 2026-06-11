import pandas as pd
import matplotlib.pyplot as plt
ages = [12, 15, 22, 25, 25, 28, 30, 32, 35, 38, 42, 45, 48, 55, 60, 62, 65, 70, 26, 29, 31]
plt.hist(ages, bins=5, color = ["orange"], edgecolor = ["black"])
#bins means to divide the data into 5 groups or intervals
plt.title("Viral Infection-Age Distribution")
plt.xlabel("Age Groups")
plt.ylabel("Number of Patients")
plt.show()