import random

# Define lists of characters to use in the password
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "="]

# Welcome message
print("Welcome to the PyPassword Generator!")

# User input for the number of letters, symbols, and numbers in the password
in_alph = int(input("How many Letter would you like in your password\n"))
in_sym = int(input("How many symbol would you like\n"))
in_num = int(input("How many numbers would you like\n"))

# Initialize an empty list to hold the password characters
passwd = []

# Add random numbers to the password
for num in range(0, in_num):
    no = random.choice(numbers)
    passwd.append(no)

# Add random letters to the password
for num in range(0, in_alph):
    al = random.choice(alphabets)
    passwd.append(al)

# Add random symbols to the password
for num in range(0, in_sym):
    sy = random.choice(symbols)
    passwd.append(sy)

# Shuffle the password list to randomize character order
random.shuffle(passwd)

# Convert the list of characters to a string
str_passwd = [str(item) for item in passwd]
hardpasswd = "".join(str_passwd)

# Display the generated password
print(f"Here is your Password: ( {hardpasswd} )")