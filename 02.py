'''
# --------------------------------------- #
#         2: STRING MANIPULATION          #
# --------------------------------------- #
Slides to reference: 2.5 Data Structures and String Manipulation

In this problem, you will practice manipulating strings. Data often requires cleaning
before it can be processed, so learning how to manipulate strings is an important part of
processing certain types of data.
'''
print("-------- Problem 2 --------")
# Continuously (in a while loop) prompt the user to enter a some input and output whether it is a palindrome.
# This while loop should continue until the user enters the word "quit".
# You can check whether "quit" is a palindrome, you don't have to go out of your way to make sure you do not.
# According to the Merriam-Webster Dictionary, a palindrome is:
#       "A word, verse, or sentence (such as "Able was I ere I saw Elba")
#       or a number (such as 1881) that reads the same backward or forward"
# Your code should be able to detect palindromes that may contain upper and lowercase characters,
# numbers, and spaces. Valid palindromes can have varying capitalization (i.e. "a" and "A" should be considered equal)
# and be split unevenly with spaces (e.g. "aa a" is a valid palindrome), but you do not 
# have to worry about the palindrome being split unevenly with punctuation.

# Some examples:
# VALID PALINDROMES:
#       - Senile felines
#       - 12321
#       - TACO Cat (Note that words will not be separated by more than one space)
#       - No lemon, no melon (Even though there is a comma, it's in the exact middle)
# NOT PALINDROMES:
#       - Mr. Owl ate my metal worm (Varying punctuation)
#       - Was it a car or a cat I saw? (Varying punctuation)
#       - 12345 (Not a palindrome)
### CODE GOES HERE, MAKE SURE TO COMMENT!###


def is_palindrome(s):
    # Clean the string: remove spaces and convert to lowercase
    cleaned_str = ''.join(s.split()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]

# Continuously prompt the user for input
while True:
    # Ask the user to input a string
    user_input = input("Enter a string (or type 'quit' to stop): ")
    
    # Exit the loop if the user types 'quit'
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    # Check if the input is a palindrome
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome!")
