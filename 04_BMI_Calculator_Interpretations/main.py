print("Let's Check Your BMI!")
height = float(input("What your height?\nMeter "))
Weight = float(input("How much your body weight? \nKG "))
bmi = round((Weight / height**2),2)
# print(f"Your BMI is {bmi}") 

if(bmi<18.5):
    print(f"Sorry, You are UNDERWEIGHT with BMI is {bmi}")
elif (bmi>25):
    print(f"Sorry, You are OVERWEIGHT with BMI is {bmi}")
else:
    print("Congrats, You are NORMAL")