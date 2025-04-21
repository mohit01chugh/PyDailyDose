# Get user input for the upper limit
enter = int(input("Enter the Num to check FizzBuzz:"))

# Loop through numbers from 1 to the entered number
for num in range(1, enter): 
    # Check if the number is divisible by both 3 and 5
    if (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")  # Print "FizzBuzz" for multiples of both
    # Check if the number is divisible by 3
    elif (num % 3 == 0):
        print("Fizz")  # Print "Fizz" for multiples of 3
    # Check if the number is divisible by 5
    elif (num % 5 == 0):
        print("Buzz")  # Print "Buzz" for multiples of 5
    else:
        print(num)  # Print the number if not divisible by 3 or 5