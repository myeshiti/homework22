'''
# --------------------------------------- #
#                5: MENU                  #
# --------------------------------------- #
Slides to reference: 2.4 Control Flow, 2.6 Functions, 2.5 Data Structures

In this final problem, you will combine everything you've learned so far!
'''

print("-------- Problem 5 --------")

'''
INTRODUCTION

After doing such a good job on Budget Bank's ATM system (even though it got hacked a few times), you've
been hired to work on an ordering system for a local restaurant! 

You've been hired to make a menu for Penny's Pizza, Pancake, and Pineapple Sorbet Parlor, 
which serves three different things:
      - Pizzas
      - Pancakes
      - Pineapple Sorbet
Penny's has a topping-based pricing model for all three items on the menu. You've already implemented most of
the ordering system for the pizzas in problem 3, so now you just need to write the ordering system for the
other two menu items and put it all together!

OBJECTIVE

You will write a menu ordering system that:
      1. Prompts the user for what they want to order
      2. Calls functions based on what the customer wants to order
      3. Returns the order and total price

DETAILS

Your program should have 4 different functions:

MENU FUNCTION - menu()
  - Prompts the user for how many items they would like to order.
  - For each item the customer wants to order, ask the user what they would like to order:
    pizza, pancake, or pineapple sorbet.
  - After the user enters a valid option (the menu should prompt again if they enter an invalid
    option), call the function dedicated to that menu item.
  - Repeat until all items are ordered.
  - Return the number of items ordered and the total price.

PIZZA FUNCTION - order_pizza()
  - You already implemented this in problem 3! You should copy your code and modify it as necessary.
  - As a refresher, this function should prompt the user for a pizza size and toppings list and calculate
    the price of the pizza. The customer may repeat toppings, but they should NOT be charged twice!
  - This function should return the price of the pizza the customer ordered.

PANCAKE FUNCTION - order_pancake()
  - This function should prompt the user for how many pancakes they want and what toppings they would
    like to add. See below for more details.
  - Again, the customer may repeat toppings by accident. Make sure you don't double charge them!
  - This function should return the price of the pancake(s) the customer ordered.

PINEAPPLE SORBET FUNCTION - order_pineapple_sorbet()
  - This function should prompt the user for how many scoops of sorbet they want and what toppings they would
    like to add. See below for more details.
  - Again, the customer may repeat toppings by accident. Make sure you don't double charge them!
  - This function should return the price of the sorbet the customer ordered.
  
ADDITIONAL NOTES
  - Don't worry about checking whether user input is valid while they are ordering items (in any order_option).
  - Customers won't order no toppings.
  - Customers won't order 0 pancakes or scoops of sorbet.
'''

# PART 1: order_pizza()
# ----------------------------------------
# Copy and edit your code from problem 3 here!
# Don't forget to write a docstring!
### CODE GOES HERE, MAKE SURE TO COMMENT!###


# PART 2: order_pancake()
# ----------------------------------------
# Pancakes are priced as follows:
# Pancakes are $2.00 each.
# The customer can add as many toppings as they would like, and they are priced as follows:
#       $0.50: Maple Syrup, Whipped Cream, Butter, Chocolate Drizzle
#       $1.00: Blueberries, Chocolate Chips, Pineapple Chunks, Banana Slices

# First, prompt the user to input how many pancakes they would like. Then, prompt them to enter their toppings.
# Toppings will be entered as a list delimited by commas and spaces.
# Your customers are forgetful and may accidentally order the same topping twice.
# However, you should not charge them twice! Each topping may only be added once!
# Don't forget to write a docstring!
### CODE GOES HERE, MAKE SURE TO COMMENT!###


# PART 3: order_pineapple_sorbet()
# ----------------------------------------
# Pineapple sorbet are priced as follows:
# Scoops of sorbet are $1.50 each.
# The customer can add as many toppings as they would like, and they are priced as follows:
#       $0.50: Whipped Cream, Chocolate Drizzle, Caramel Drizzle
#       $1.00: Sprinkles, Gummy Bears, Cherry, Pineapple Chunks
#       $4.00: Served in a pineapple

# First, prompt the user to input how many scoops they would like. Then, prompt them to enter their toppings.
# Then, ask whether they would like the sorbet served in a pineapple (yes/no answer).
# Toppings will be entered as a list delimited by commas and spaces.
# Your customers are forgetful and may accidentally order the same topping twice.
# However, you should not charge them twice! Each topping may only be added once!
# Don't forget to write a docstring!
### CODE GOES HERE, MAKE SURE TO COMMENT!###



# PART 4: menu()
# ----------------------------------------
# First, prompt the user to enter how many items they would like to order.
# The customer can order multiple of each item! For example, three pizzas and one pineapple sorbet is valid.
# For every item they would like to order, ask the user which item they would like to order.
# Input will be in the form of a number:
#     1. Pizza
#     2. Pancake
#     3. Pineapple Sorbet
# If the user enters an invalid option (anything other than "1", "2", or "3"), prompt again. 
# After the user makes their choice, call the appropriate function. The function should return the price
# of that item.
# Repeat until all items are ordered.
# Print the amount of items ordered and the total price.
# Don't forget to write a docstring!
### CODE GOES HERE, MAKE SURE TO COMMENT!###
# PART 1: order_pizza()
# ----------------------------------------
def order_pizza():
    """
    This function handles pizza orders. It prompts the user for pizza size and toppings,
    calculates the price based on the size and toppings, and returns the total price.

    Returns:
    float: The total price of the pizza with toppings.
    """
    pizza_prices = {'small': 5.00, 'medium': 8.00, 'large': 10.00}
    topping_prices = {'corn': 0.50, 'onions': 0.50, 'bell peppers': 0.50, 'olives': 0.50,
                      'spinach': 1.00, 'mushrooms': 1.00, 'anchovies': 1.00, 'pineapple': 1.00,
                      'pepperoni': 1.50, 'sausage': 1.50, 'chicken': 1.50, 'ham': 1.50}

    # Get pizza size from the user
    size = input("What size pizza would you like? (small, medium, large): ").lower()
    while size not in pizza_prices:
        size = input("Invalid size. Please enter small, medium, or large: ").lower()

    # Get toppings from the user
    toppings = input("Enter your toppings (comma separated): ").lower().split(", ")
    unique_toppings = set(toppings)  # Remove duplicate toppings
    total_price = pizza_prices[size] + sum(topping_prices[topping] for topping in unique_toppings)

    return total_price


# PART 2: order_pancake()
# ----------------------------------------
def order_pancake():
    """
    This function handles pancake orders. It prompts the user for the number of pancakes 
    and their toppings, calculates the price based on the number of pancakes and toppings,
    and returns the total price.

    Returns:
    float: The total price of the pancakes with toppings.
    """
    pancake_price = 2.00
    topping_prices = {'maple syrup': 0.50, 'whipped cream': 0.50, 'butter': 0.50, 'chocolate drizzle': 0.50,
                      'blueberries': 1.00, 'chocolate chips': 1.00, 'pineapple chunks': 1.00, 'banana slices': 1.00}

    # Get number of pancakes from the user
    num_pancakes = int(input("How many pancakes would you like? "))
    
    # Get toppings from the user
    toppings = input("Enter your toppings (comma separated): ").lower().split(", ")
    unique_toppings = set(toppings)  # Remove duplicate toppings
    total_price = num_pancakes * pancake_price + sum(topping_prices[topping] for topping in unique_toppings)

    return total_price


# PART 3: order_pineapple_sorbet()
# ----------------------------------------
def order_pineapple_sorbet():
    """
    This function handles pineapple sorbet orders. It prompts the user for the number of scoops 
    and their toppings, calculates the price based on the number of scoops and toppings,
    and returns the total price. It also asks if they want the sorbet served in a pineapple.

    Returns:
    float: The total price of the sorbet with toppings and the optional pineapple.
    """
    sorbet_price = 1.50
    topping_prices = {'whipped cream': 0.50, 'chocolate drizzle': 0.50, 'caramel drizzle': 0.50,
                      'sprinkles': 1.00, 'gummy bears': 1.00, 'cherry': 1.00, 'pineapple chunks': 1.00}
    pineapple_price = 4.00

    # Get number of scoops from the user
    num_scoops = int(input("How many scoops of pineapple sorbet would you like? "))
    
    # Get toppings from the user
    toppings = input("Enter your toppings (comma separated): ").lower().split(", ")
    unique_toppings = set(toppings)  # Remove duplicate toppings

    # Ask if they want it served in a pineapple
    pineapple_option = input("Would you like it served in a pineapple? (yes/no): ").lower()
    if pineapple_option == "yes":
        total_price = (num_scoops * sorbet_price) + sum(topping_prices[topping] for topping in unique_toppings) + pineapple_price
    else:
        total_price = (num_scoops * sorbet_price) + sum(topping_prices[topping] for topping in unique_toppings)

    return total_price


# PART 4: menu()
# ----------------------------------------
def menu():
    """
    This function serves as the main menu for the ordering system. It prompts the user to 
    choose how many items they would like to order and allows them to choose between pizza,
    pancakes, and pineapple sorbet. It calls the corresponding order function for each item 
    and calculates the total price for all items ordered.
    """
    total_price = 0.0
    num_items = int(input("How many items would you like to order? "))

    for _ in range(num_items):
        order_type = input("What would you like to order? (1. Pizza, 2. Pancake, 3. Pineapple Sorbet): ")
        
        while order_type not in ["1", "2", "3"]:
            order_type = input("Invalid option. Please enter 1, 2, or 3: ")
        
        if order_type == "1":
            total_price += order_pizza()
        elif order_type == "2":
            total_price += order_pancake()
        elif order_type == "3":
            total_price += order_pineapple_sorbet()

    print(f"\nYou ordered {num_items} item(s). Your total price is: ${total_price:.2f}")


# Some extra code to run your functions, don't worry about it!
def main():
    menu()

if __name__ == "__main__":
    main()
