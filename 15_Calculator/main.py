print('''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

''')

# Options for mathematical operations
opts = '''
            +\n
            -\n
            *\n
            /\n
                '''

import os

# Get the first number from the user
in1 = float(input("What's the first number?:  "))

def cal():    
    # Display operation options and get the chosen operation
    print(opts)
    opt = input("Pick an operation:  ")
    
    # Get the second number from the user
    in2 = float(input("What's the next number?: "))   
    
    # Perform the calculation based on the chosen operation
    if opt == "+":
        ot = in1 + in2    
    elif opt == "-":
        ot = in1 - in2   
    elif opt == "*":
        ot = in1 * in2   
    elif opt == "/":
        ot = in1 / in2   
    else:
        print("Please Enter a Valid Operator.")

    # Display the result of the calculation
    print(f"{in1} {opt} {in2} = {ot}")
    return ot

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

cal_continue = True

# Loop to continue calculations
while cal_continue:
    ot = cal()       
    # Ask user if they want to continue with the result or start a new calculation
    in4 = input(f"Type 'y' to continue calculating with {ot}, or type 'n' to start a new calculation: ")
    if in4 == "y":
         in1 = ot  # Use the result for the next calculation          
    else:
          clear_screen()  # Clear the screen for a new calculation
          in1 = float(input("What's the first number?:  "))  # Get a new first number