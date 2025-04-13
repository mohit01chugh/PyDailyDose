# Welcome message
print("Welcome to the tip Calculator!")

# Get the total bill amount from the user
bill = float(input("What was the total bill? \n $"))

# Get the tip percentage from the user
tip = int(input("How much tip would you like to give? 10%, 12%, 15% or more? \n %"))

# Calculate the total bill including the tip
total_bill = bill + (bill * (tip / 100))

# Display the total bill
print(total_bill)

# Get the number of people to split the bill
split_bill = int(input("How many people to split the bill? \n"))

# Calculate the amount each person should pay
final_amt = round((total_bill / split_bill), 2)

# Display the final amount each person should pay
print(f"Each person should pay: $ {final_amt}")