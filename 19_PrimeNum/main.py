def is_prime(num):
    # Check if the number is 2 (the only even prime number)
    if num == 2:
        return True
    # Check if the number is 1 (not prime)
    if num == 1:
        return False
 
    # Check for factors from 2 to num-1
    for i in range(2, num):
        if num % i == 0:  # If num is divisible by i, it's not prime
            return False
    return True  # If no factors found, num is prime

# Test the function with the number 7
print(is_prime(7))  # Expected output: True