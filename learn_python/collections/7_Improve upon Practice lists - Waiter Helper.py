# Outcome (By doing this you should): Practice using lists and dictionaries
# Script should act like a waiter at a restaurant taking orders
# level 1
# Greet the user
user_name = input("What's your name? ")
print("Good Day " + user_name)

# Print a list of starters
starters_list = ["Mixed Olives",
                 "Garlic Bread",
                 "Garlic Mushrooms"]
print(f"Your starters choices are: {starters_list}")

# Take an input for the user for their starter
user_starters_choice = ""

''' A long winded version but gives some user feedback as to why they're being asked again
while starters_list.count(user_starters_choice) == 0: # while the starter choice is not listed in the list... ask for the starter
    user_starters_choice = input("What would you like for your starter? ")
    if user_starters_choice not in starters_list :
        print("Please choose a valid option.")
'''

while user_starters_choice not in starters_list:
    user_starters_choice = input("What would you like for your starter? ")


# Print a list of mains
mains_list = ["Pasta with Pizzaiola Sauce",
              "Pork Chop",
              "Sirloin Steak"]
print(f"Your mains choices are: {mains_list}")

# Take an input for the user for their main course
user_mains_choice = ""
while user_mains_choice not in mains_list:
    user_mains_choice = input("What would you like for your main? ")

# Print a list of desserts
desserts_list = ["Affogato",
                 "Eton Mess",
                 "Chef's Cheesecake of the Day"]
print(f"Your starters choices are: {desserts_list}")

# Take an input for the user for their dessert
user_desserts_choice = ""
while user_desserts_choice not in desserts_list:
    user_desserts_choice = input("What would you like for your dessert? ")

# Print all of the user's choices
print(f"So you've gone for the {user_starters_choice} as your starter. \n"
      f"Then you've decided on the {user_mains_choice} as your mains. \n"
      f"And finally for your dessert you have chosen {user_desserts_choice}.")

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'
customer_order_list = [user_starters_choice, user_mains_choice, user_desserts_choice]

# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
starters_dic_list = {"Mixed Olives" : "6.99",
                     "Garlic Bread" : "7.99",
                     "Garlic Mushrooms" : "8.99"}

mains_dic_list = {"Pasta with Pizzaiola Sauce" : "15.99",
                  "Pork Chop" : "17.99",
                  "Sirloin Steak" : "18.99"}

desserts_dic_list = {"Affogato" : "6.99",
                     "Eton Mess" : "7.99",
                     "Chef's Cheesecake of the Day" : "8.99"}

starter_price = starters_dic_list[(customer_order_list[0])]
main_price = mains_dic_list[(customer_order_list[1])]
dessert_price = desserts_dic_list[(customer_order_list[2])]
user_bill = float(starter_price) + float(main_price) + float(dessert_price)

print(f"Your bill comes to £{user_bill}")

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
# TODO enclose in loop that allows for asking the user if they'd like to order more? OR ask if they would like to order more than one dish after ordering each course, which is more natural