import pandas as pd
import matplotlib.pyplot as plt
ages = [12, 15, 22, 25, 25, 28, 30, 32, 35, 38, 42, 45, 48, 55, 60, 62, 65, 70, 26, 29, 31]
plt.hist(ages, bins=5, color = ["orange"], edgecolor = ["black"])
#bins yani 5 piller me todna hai
plt.title("Viral Infection-Age Distribution")
plt.xlabel("Age Gruops")
plt.ylabel("Number of Patients")
plt.show()