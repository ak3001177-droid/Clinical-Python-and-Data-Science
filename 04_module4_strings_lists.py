# ==========================================
# FILE 1: STRINGS & LISTS MASTERCLASS
# ==========================================

# ---------------------------------------------------------
# CONCEPT 1: STRING PARSING & FILTERING (.split, .isalpha, .strip)
# ---------------------------------------------------------
def sales_prices(item_and_price):
    """Separates item names (words) from their prices (numbers)"""
    item = ""
    price = ""
    # String ko list mein todna
    item_or_price = item_and_price.split()
    
    for x in item_or_price:
        if x.isalpha():  # Agar sirf alphabets hain
            item += x + " "
        else:            # Agar number ya symbol hai
            price = x
            
    # Aakhiri extra space ko kaatna
    item = item.strip()
    return "{} are on sale for ${}".format(item, price)

print("--- Concept 1 ---")
print(sales_prices("Winter fleece jacket 49.99"))


# ---------------------------------------------------------
# CONCEPT 2: STRING REPLACEMENT (.replace, .upper)
# ---------------------------------------------------------
def highlight_word(sentence, word):
    """Finds a specific word and converts it to UPPERCASE"""
    return sentence.replace(word, word.upper())

print("\n--- Concept 2 ---")
print(highlight_word("Automating with Python is fun", "fun"))


# ---------------------------------------------------------
# CONCEPT 3: LIST METHODS (.sort, .reverse, .insert)
# ---------------------------------------------------------
def sort_distance(distances):
    """Sorts a list in descending order"""
    distances.sort(reverse=True) # Sort aur reverse dono ek sath!
    return distances

print("\n--- Concept 3 ---")
my_distances = [2, 4, 0, 15, 8, 9]
print("Sorted distances:", sort_distance(my_distances))

# List ke beech mein kuch ghusana (insert)
colors = ["red", "white", "blue"]
colors.insert(2, "yellow") # Index 2 par yellow bitha diya
print("Updated colors:", colors)


# ---------------------------------------------------------
# CONCEPT 4: LIST COMPREHENSION (Range with Math)
# ---------------------------------------------------------
def increments(start, end):
    """Creates a list with n+2 for a specific range"""
    # Range mein end+1 lagaya taaki aakhiri number bhi include ho
    return [n + 2 for n in range(start, end + 1)]

print("\n--- Concept 4 ---")
print("Increments for (2, 3):", increments(2, 3))