# Welcome message
print("Let's Check Your BMI!")

# Get height in meters with input validation
while True:
    try:
        height = float(input("Enter your height in meters (e.g., 1.75): "))
        if height <= 0:
            print("Height must be a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number for height.")

# Get weight in kilograms with input validation
while True:
    try:
        weight = float(input("Enter your weight in kilograms (e.g., 70): "))
        if weight <= 0:
            print("Weight must be a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number for weight.")

# Calculate BMI
bmi = round((weight / height**2), 2)

# Display BMI
print(f"Your BMI is {bmi}")

# Optional: Interpret BMI
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")