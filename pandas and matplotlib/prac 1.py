import pandas as pd
import matplotlib.pyplot as plt

blood_group = {
    "blood_gp" : ["A+", "B+", "O+", "AB+"],
    "unites" : [25, 40, 60, 15]
}
df = pd.DataFrame(blood_group)
plt.bar(df["blood_gp"], df["unites"], color = ["red", "blue"])
plt.title("Blood Bank Stock Report")
plt.xlabel("Blood Group")
plt.ylabel("Unites")
plt.savefig("blood_bank_report.png")
plt.show()