'''
# --------------------------------------- #
#           4: FUNCTION PRACTICE          #
# --------------------------------------- #
Slides to reference: 2.6 Functions

In this problem, you will practice writing and using functions. 
Functions allow us to break code into reusable blocks and return useful values.

You will be writing two functions:
    - One to check if a password meets common strength requirements.
    - One to interact with the user and validate their input.
'''

print("-------- Problem 4 --------")

# Part 1: is_valid_password(password)
# ----------------------------------------
# Write a function called `is_valid_password` that checks if a password is strong.
# A valid password must:
#    - Be at least 8 characters long
#    - Include at least one uppercase letter
#    - Include at least one lowercase letter
#    - Include at least one number
#
# If the password meets all requirements, return True.
# Otherwise, print what it's missing and return False.
# Remember to write a docstring for the function!
### CODE GOES HERE, MAKE SURE TO COMMENT!###


# Part 2: password_helper()
# ----------------------------------------
# Write a function called `password_helper` that:
#   - Continuously (in a while loop) prompts the user to enter a password using input()
#   - This while loop should continue until the user enters the word "quit".
#    - You can check whether "quit" is a valid password, 
#      you don't have to go out of your way to make sure you do not.
#   - Calls your is_valid_password() function
#   - Prints "Password is valid!" or "Password is invalid."
#
# This function does not return anything.
# You may assume the user enters a string.
### CODE GOES HERE, MAKE SURE TO COMMENT!###

def is_valid_password(password):
    """
    This function checks if a password meets the following requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one number

    Args:
    password (str): The password to validate.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
    
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        return False
    
    # If all conditions are met
    return True

# Example of usage
password = input("Enter a password to validate: ")
if is_valid_password(password):
    print("Your password is valid!")
else:
    print("Your password is not valid.")
# Some extra code to run your functions, don't worry about it!
def main():
  password_helper()

if __name__ == "__main__":
    main()
