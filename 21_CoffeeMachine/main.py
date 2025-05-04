# Coffee recipes with ingredients and cost
coffee_recipes = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "cost": 1.5
    },
    "latte": {
        "water": 200,
        "coffee": 18,
        "milk": 150,
        "cost": 2.5
    },
    "cappuccino": {
        "water": 200,
        "coffee": 18,
        "milk": 100,
        "cost": 2.0
    }
}

# Available resources
resources = {
    "water": 500,
    "milk": 500,
    "coffee": 100,
}

# Total sales variable
sale = 0

# Function to process coins inserted by the user
def process_coins():
    print("Please Insert the Coins")
    c1 = int(input("How many quarters: "))
    c2 = int(input("How many dimes: "))
    c3 = int(input("How many nickels: "))
    c4 = int(input("How many pennies: "))
    total = (0.25 * c1) + (0.10 * c2) + (0.05 * c3) + (0.01 * c4)  # Calculate total amount
    print(total)
    return total

# Function to handle the transaction for the selected coffee
def transaction(coffee_type):
    global sale
    total = process_coins()  # Get the total amount inserted
    # Check if the total is sufficient for the coffee
    if (total == coffee_recipes[coffee_type]["cost"]) or \
         (total > coffee_recipes[coffee_type]["cost"]):
        if total > coffee_recipes[coffee_type]["cost"]:
            change = round(total - coffee_recipes[coffee_type]["cost"], 2)  # Calculate change
            print(f"Inserted too much money. Here is your change: ${change} refunded.")
        print("Here is your " + coffee_type + ". Enjoy!")  # Serve the coffee
        # Deduct resources used for the coffee
        resources["water"] -= coffee_recipes[coffee_type]["water"]
        resources["milk"] -= coffee_recipes[coffee_type]["milk"]
        resources["coffee"] -= coffee_recipes[coffee_type]["coffee"]
        sale += coffee_recipes[coffee_type]["cost"]  # Update total sales
    elif total < coffee_recipes[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")  # Insufficient funds
    
    return sale

# Function to check if resources are sufficient for the selected coffee
def resources_sufficient(coffee_type):
    for item in ["water", "milk", "coffee"]:
        if coffee_recipes[coffee_type][item] > resources[item]:  # Check each resource
            print(f"Sorry there is not enough {item}. Inform to Admin")
            return False
    return True

# Main loop for coffee machine operation
continue_coffee = True
while continue_coffee:
    incr = input("What would you like? (espresso/latte/cappuccino): ").lower()  # User input for coffee type

    if incr in coffee_recipes:  # Check if the input is a valid coffee type
        if resources_sufficient(incr):  # Check if resources are sufficient
            transaction(incr)  # Process the transaction
    elif incr == "off":  # Turn off the coffee machine
        continue_coffee = False  
    elif incr == "report":  # Print current resources and sales report
        print(f"Status\nWater: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g\nMoney: ${sale}")
    else:
        print("Invalid Input")  # Handle invalid input
