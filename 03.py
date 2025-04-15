'''
# --------------------------------------- #
#            3: DATA STRUCTURES           #
# --------------------------------------- #
Slides to reference: 2.5 Data Structures and String Manipulation

In this problem, you will practice using 3 types of data structures:
      - Lists are ordered collections of items that can be resized and hold multiple datatypes.
      - Dictionaries are a mutable collection of key value pairs that map a unique, immutable key onto some value.
      - Sets are mutable sets of immutable, unique, and unordered elements.
'''
print("-------- Problem 3 --------")
# Write a program that takes a pizza order and outputs the order and the price of the order.
# Pizzas are priced as follows:
# Small pizzas start at $5, medium pizzas start at $8, and large pizzas start at $10.
# The customer can add as many toppings as they would like, and they are priced as follows:
#       $0.50: Corn, Onions, Bell Peppers, Olives
#       $1.00: Spinach, Mushrooms, Anchovies, Pineapple
#       $1.50: Pepperoni, Sausage, Chicken, Ham

# First, prompt the user to input their desired pizza size. Then, prompt them to enter their toppings.
# Toppings will be entered as a list delimited by commas and spaces (", ").
# Your customers are forgetful and may accidentally order the same topping twice.
# However, you should not charge them twice! Each topping may only be added once!
# Sample input + output:
#     INPUT:
#     Medium
#     Onions, Mushrooms, Olives, Ham, Spinach, Mushrooms, Corn
#     OUTPUT:
#     You ordered a medium pizza with 6 topping[s]. Your total is $13.00.
### CODE GOES HERE, MAKE SURE TO COMMENT!###

pizza_prices = {
    "small": 5.00,
    "medium": 8.00,
    "large": 10.00
}

# Topping prices
topping_prices = {
    "Corn": 0.50,
    "Onions": 0.50,
    "Bell Peppers": 0.50,
    "Olives": 0.50,
    "Spinach": 1.00,
    "Mushrooms": 1.00,
    "Anchovies": 1.00,
    "Pineapple": 1.00,
    "Pepperoni": 1.50,
    "Sausage": 1.50,
    "Chicken": 1.50,
    "Ham": 1.50
}

# Prompt the user to input their desired pizza size
pizza_size = input("Enter pizza size (small, medium, large): ").lower()

# Ensure the pizza size is valid
while pizza_size not in pizza_prices:
    print("Invalid pizza size! Please enter 'small', 'medium', or 'large'.")
    pizza_size = input("Enter pizza size (small, medium, large): ").lower()

# Prompt the user to input toppings
toppings_input = input("Enter your toppings (comma-separated): ")

# Split the toppings input into a list and remove any leading/trailing spaces
toppings_list = [topping.strip() for topping in toppings_input.split(",")]

# Convert the list to a set to remove duplicates
unique_toppings = set(toppings_list)

# Calculate the total cost
total_cost = pizza_prices[pizza_size]  # Start with the base price for the pizza

# Add the cost of the toppings
for topping in unique_toppings:
    if topping in topping_prices:
        total_cost += topping_prices[topping]

# Print the order summary
num_toppings = len(unique_toppings)  # Count of unique toppings
print(f"You ordered a {pizza_size} pizza with {num_toppings} topping[s]. Your total is ${total_cost:.2f}.")
