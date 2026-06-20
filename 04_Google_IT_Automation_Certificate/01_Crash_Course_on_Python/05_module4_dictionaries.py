# ==========================================
# FILE 2: DICTIONARY OPERATIONS MASTERCLASS
# ==========================================

# ---------------------------------------------------------
# CONCEPT 1: DICTIONARY COPY & OVERWRITE (.copy)
# ---------------------------------------------------------
def reset_scores(game_scores):
    """Creates a safe copy of scores and resets them to 0"""
    # Original data ko bachane ke liye photocopy banayi
    new_game_scores = game_scores.copy() 
    
    for player, score in new_game_scores.items():
        # Purane score ko overwrite karke 0 kar diya
        new_game_scores[player] = 0
        
    return new_game_scores

print("--- Concept 1 ---")
game1_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}
print("Original Scores:", game1_scores)
print("Reset Scores:", reset_scores(game1_scores))


# ---------------------------------------------------------
# CONCEPT 2: FREQUENCY COUNTER (The "Register" Logic)
# ---------------------------------------------------------
def count_letters(text):
    """Counts how many times each alphabet appears in a string"""
    dictionary = {}
    
    for letter in text.lower():
        # Bouncer/Guard: Sirf alphabets andar aayenge
        if letter.isalpha():
            
            # Plan A: Agar naya letter hai, toh naya panna banao
            if letter not in dictionary:
                dictionary[letter] = 0
                
            # Plan B: Count badhate jao
            dictionary[letter] += 1
            
    return dictionary

print("\n--- Concept 2 ---")
print("Letter Count:", count_letters("Math is fun! 2+2=4"))


# ---------------------------------------------------------
# CONCEPT 3: ITERATING & FORMATTING DICTIONARIES
# ---------------------------------------------------------
def car_listing(car_prices):
    """Iterates through dictionary and formats a clean sentence"""
    result = ""
    
    for car_model, car_price in car_prices.items():
        # Dhyan rahe: '\n' aur '.format' ke beech koi space nahi hona chahiye!
        result += "A {} costs {} dollars.\n".format(car_model, car_price)
        
    return result

print("\n--- Concept 3 ---")
cars = {"Kia Soul": 19000, "Ford Fiesta": 13000}
print(car_listing(cars))