import sys

# Welcome message
print("Welcome to Express Pizza Deliveries")

# Prompt user for pizza size
size = input("What size pizza do you want? S, M, L:\n")
# Determine pizza cost based on size
if (size == "S"):
    pizza_cost = 15
    print("Small Pizza: $15")
elif (size == "M"):
    pizza_cost = 20
    print("Medium Pizza: $20")
elif (size == "L"):
    pizza_cost = 25
    print("Large Pizza: $25")
else:
    # Exit if invalid size is entered
    print("You typed the wrong input")
    sys.exit()
    
# Ask if the user wants pepperoni
pepperonic = input("Do you want pepperoni on your pizza? Y or N:\n")
# Calculate cost with pepperoni
if (pepperonic == "Y" and size == "S"):
    cost_with_pep = pizza_cost + 2  # Small pizza with pepperoni
elif (pepperonic == "Y" and (size == "M" or size == "L")):
    cost_with_pep = pizza_cost + 3  # Medium or large pizza with pepperoni
else:
    cost_with_pep = pizza_cost  # No pepperoni

# Ask if the user wants extra cheese
extra_cheese = input("Do you want extra cheese? Y or N:\n")    
# Calculate final bill based on extra cheese
if (extra_cheese == "Y"):
    bill = cost_with_pep + 1  # Add cost for extra cheese
else:
    bill = cost_with_pep  # No extra cheese

# Display the final bill
print(f"Your Final bill is ${bill}")