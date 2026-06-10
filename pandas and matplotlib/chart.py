import matplotlib.pyplot as plt

# 1. Apna nakli data banate hain
machines = ['X-Ray', 'CT Scan', 'MRI', 'PET']
patients = [45, 20, 15, 5]

# 2. Bar Chart banane ka command, sath mein colors bhi set kiye hain
plt.bar(machines, patients, color=['red', 'blue', 'green', 'orange'])
# phli jagah par x axis ke labels, dusri jagah par y axis ke values, aur teesri jagah par bar ke colors diye gaye hain

# 3. Chart ko title aur labels dena
plt.title("Daily Patient Scans (Mock Data)")
plt.xlabel("Machine Ka Naam")
plt.ylabel("Number of Patients")

# 4. Chart ko screen par dikhane ka aakhiri command (Yeh sabse zaroori hai)
plt.show()