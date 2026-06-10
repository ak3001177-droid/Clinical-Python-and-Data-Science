class Medicine:
    def __init__(self, name, stock, expiery_year):
        self.name = name
        self.stock = stock
        self.exp = expiery_year

    def is_safe_to_use(self, current_year):
        if (self.exp <= current_year):
            return False
        else:
            return True
        
Med_list = [
    Medicine("para", 50, 2025),
    Medicine("you", 10, 2028),
    Medicine("i", 2, 2024)
]   

safe_count = 0
current_year = 2024
for m in Med_list:
    if m.is_safe_to_use(current_year) == True:
        safe_count+=1

print("Safe to use:", safe_count)        
