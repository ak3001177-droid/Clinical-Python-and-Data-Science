import pandas as pd
import matplotlib.pyplot as plt

# 1. Pandas ke zariye ek nakli data table (DataFrame) banate hain
data = {
    'Hospital_Dept': ['Radiology', 'Pathology', 'Emergency', 'Surgery'],
    'Total_Patients': [150, 200, 350, 80]
}
df = pd.DataFrame(data)

# 2. Ab Pandas ka data seedha Matplotlib mein daalte hain
# X-axis par Department ka naam, Y-axis par Patients ki ginti
# Bar Chart banana aur usko ek naam 'bars' dena
bars = plt.bar(df['Hospital_Dept'], df['Total_Patients'], color=['purple', 'teal', 'orange', 'red'])
# yha double comma bhi lga sakte hai

# 3. THE MAGIC TRICK: Har bar ke upar uska exact number print karna
# padding=3 aur fontweight='bold': Yeh thoda sa 'Makeup' hai. padding=3 ka matlab hai number bar ke bilkul
#  upar chipka na ho, thoda sa space (gap) ho. Aur bold se number dark aur clear dikhega.
plt.bar_label(bars, padding=3, fontweight='bold')

# 3. Chart ki formatting
plt.title("Hospital Patient Load (Pandas + Matplotlib)")
plt.xlabel("Departments")
plt.ylabel("Patient Count")

# 4. Show Chart
plt.show()