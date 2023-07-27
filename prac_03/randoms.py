import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Line 1 used random.randint(5, 20). This will print a random integer between 5 and 20, inclusive.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5, and the largest is 20.

# What did you see on line 2?
# Line 2 used random.randrange(3, 10, 2). This will print a random integer from the range [3, 10) with a step of 2.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3, and the largest is 9. That 10 is not included in the range due to the half-open interval.

# Could line 2 have produced a 4?
# No, it could not have produced a 4. The step size is 2, and the range starts from 3. Therefore, the possible numbers are 3, 5, 7, and 9.

# What did you see on line 3?
# Line 3 used random.uniform(2.5, 5.5). This will print a random floating-point number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.5, and the largest is 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

random_number = random.randint(1, 101)
print(random_number)
