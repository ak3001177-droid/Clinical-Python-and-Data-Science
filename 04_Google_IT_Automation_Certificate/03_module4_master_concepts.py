# ==========================================
# CONCEPT 1: TUPLES & MULTIPLE RETURN VALUES
# ==========================================
def calculate_patient_stats(height, weight):
    """Returns multiple values as a tuple"""
    bmi = weight / (height ** 2)
    diff = weight - 60
    return bmi, diff  # Python automatically makes this a tuple (bmi, diff)

# Unpacking the returned tuple into separate variables
patient_bmi, weight_diff = calculate_patient_stats(1.75, 70)
print(f"BMI: {patient_bmi}, Difference: {weight_diff}")

# ==========================================
# CONCEPT 2: TUPLES WITH MUTABLE OBJECTS
# ==========================================
# Tuple itself cannot be changed, but the list inside it CAN be changed.
my_tuple = (1, 2, ['a', 'b', 'c'])
my_tuple[2][0] = 'x'  
# my_tuple is now: (1, 2, ['x', 'b', 'c'])

# ==========================================
# CONCEPT 3: LIST COMPREHENSION (The 1-Line Magic)
# ==========================================
# Example A: Basic Loop
multiples_of_7 = [x * 7 for x in range(1, 11)]

# Example B: List Comprehension with ONLY 'If' (Filtering)
# Returns odd numbers only
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]

# Example C: List Comprehension with 'If-Else' (Replacing)
# Renaming .hpp files to .h, leaving others alone
old_files = ["program.c", "stdio.hpp", "math.hpp", "a.out"]
updated_files = [file.replace(".hpp", ".h") if file.endswith(".hpp") else file for file in old_files]

# Example D: Loop with Tuple Unpacking & Formatting
people = [("alex@hospital.com", "Alex Diego"), ("shay@hospital.com", "Shay Brandt")]
formatted_emails = ["{} <{}>".format(name, email) for email, name in people]

# ==========================================
# CONCEPT 4: DICTIONARY ITERATION & INVERSION
# ==========================================
def invert_system_groups(group_dictionary):
    """Takes a dict of {Group: [Users]} and returns {User: [Groups]}"""
    user_groups = {}
    
    # .items() un-packs the dictionary into key and value
    for group, users in group_dictionary.items():
        for user in users:
            # Plan A: User already exists, append to their list
            if user in user_groups:
                user_groups[user].append(group)
            # Plan B: New user, create a new list for them
            else:
                user_groups[user] = [group]
                
    return user_groups

system_data = {"local": ["admin", "userA"], "public": ["admin", "userB"]}
print(invert_system_groups(system_data))
# Outputs: {'admin': ['local', 'public'], 'userA': ['local'], 'userB': ['public']}