# patient_triage_system.py
# Concepts Covered: Variables, Data Types, Functions, Conditionals (if/elif/else), Logical/Comparison Operators

def assess_patient_priority(patient_name, age, oxygen_level, has_chest_pain):
    """
    This function evaluates patient vitals and returns the emergency priority level.
    Demonstrates: Function definition, Parameters, and Return values.
    """
    print("--- Triage Assessment Started for: " + patient_name + " ---")
    
    # Demonstrating Comparison and Logical Operators (and / or / == / < / >)
    if oxygen_level < 90 or has_chest_pain == True:
        return "CRITICAL: Allocate ICU Bed Immediately!"
        
    elif age >= 60 and oxygen_level <= 95:
        return "HIGH: Keep under continuous observation."
        
    elif oxygen_level > 95 and has_chest_pain == False:
        return "NORMAL: Send to General Ward OPD."
        
    else:
        return "MODERATE: Wait in the queue for doctor's checkup."

# ---------------------------------------------------------
# Main Execution Block
# Demonstrating Variables, Data Types, and Type Conversion
# ---------------------------------------------------------

# Patient 1 Data
p1_name = "Ramesh Kumar"
p1_age = 65
p1_o2_level = 93
p1_chest_pain = False

# Patient 2 Data
p2_name = "Suresh Singh"
p2_age = 45
p2_o2_level = 88
p2_chest_pain = True

# Calling the function and storing the returned value
p1_status = assess_patient_priority(p1_name, p1_age, p1_o2_level, p1_chest_pain)

# Explicit type conversion using str() to combine text and numbers
print("Age: " + str(p1_age) + " | Priority: " + p1_status)
print("\n") # Adding a blank line for readability

# Testing the second patient
p2_status = assess_patient_priority(p2_name, p2_age, p2_o2_level, p2_chest_pain)
print("Age: " + str(p2_age) + " | Priority: " + p2_status)