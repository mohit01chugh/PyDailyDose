# Welcome message
print("Let's Check Your BMI!")

# Get height in meters
height = float(input("Enter your height in meters (e.g., 1.75): "))
        
# Get weight in kilograms
weight = float(input("Enter your weight in kilograms (e.g., 70): "))
        
# Calculate BMI
bmi = round((weight / height**2), 2)

# Display BMI
print(f"Your BMI is {bmi}")
