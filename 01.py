'''
# --------------------------------------- #
#            1: CONTROL FLOW              #
# --------------------------------------- #
Slides to reference: 2.4 Control Flow

In this problem, you will practice using two useful loops:
     - For loops use a counter to track iterations and run a set amount of times.
     - While loops run a variable amount of times based on a condition.

You aren't expected to use break/continue/pass in this particular problem but
they are useful, so be sure you know how to use them!
'''
print("-------- Problem 1 --------")
# Prompt the user to input two numbers. The numbers will be input on two different lines. 
# The first number should be smaller than the second.
# (You should check if this is the case and prompt the user to enter a valid range if it is not.)
# Then, print all prime numbers between those two numbers, inclusive.
### CODE GOES HERE, MAKE SURE TO COMMENT!###
# Input the first number
start_num = int(input("Enter the first number: "))

# Input the second number
end_num = int(input("Enter the second number: "))

# Check if the first number is smaller than the second
while start_num >= end_num:
    print("The first number must be smaller than the second number. Please enter again.")
    start_num = int(input("Enter the first number: "))
    end_num = int(input("Enter the second number: "))

# Now, let's find all prime numbers between start_num and end_num

# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
print(f"Prime numbers between {start_num} and {end_num} are:")

# Iterate over the range of numbers (inclusive)
for num in range(start_num, end_num + 1):
    # Skip numbers less than 2, because they aren't prime
    if num < 2:
        continue
    
    # Check if num is a prime number
    is_prime = True  # Assume num is prime
    for i in range(2, int(num ** 0.5) + 1):  # Loop to check divisibility up to the square root of num
        if num % i == 0:  # If num is divisible by any number other than 1 and itself
            is_prime = False
            break  # Exit the loop early since we already know it's not prime
    
    # If the number is prime, print it
    if is_prime:
        print(num)


