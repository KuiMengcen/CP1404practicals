"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    while denominator == 0:
        denominator = int(input("Enter the denominator again: "))
print("Finished.")

# 1. The ValueError will occur if the user enters non-integer values for the numerator or denominator. For example, if the user enters a string or any non-numeric value.

# 2. The ZeroDivisionError will occur if the user enters 0 as the denominator since dividing any number by 0 is not allowed in mathematics.

# 3. To avoid the possibility of a ZeroDivisionError, you can add a condition to check if the denominator is 0 before performing the division. If the denominator is 0, you can handle it separately and ask the user to enter a valid denominator.