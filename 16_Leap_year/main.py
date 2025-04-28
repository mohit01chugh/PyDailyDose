def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                print("True")  # Year is a leap year
            else:
                print("False")  # Year is not a leap year
        else:
            print("True")  # Year is a leap year
    else:
        print("False")  # Year is not a leap year

# Test cases
is_leap_year(2000)  # True
is_leap_year(2100)  # False
is_leap_year(2400)  # True
is_leap_year(1989)  # False
is_leap_year(1992)  # True