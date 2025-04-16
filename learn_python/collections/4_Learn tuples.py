# How are tuples similar to lists?
# Tuples are similar to lists in that you can list values and store them in one variable

# Are tuples immutable and what does this mean?
# Tuples are immutable as they cannot be changed once they have been made

# What other data types are immutable?
# strings, integers, booleans,

# What are good use cases for tuples instead of lists?
# protected once made

# What does the following piece of code do?
essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))

# ---

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3) # YOUR CODE GOES HERE INSTEAD OF 'None'
# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
# YOUR CODE GOES HERE
essentials_tuple = list(essentials_tuple)
essentials_tuple.append(essential_item4)
essentials_tuple = tuple(essentials_tuple)
print("Here are your items as a tuple (with the 4th item added):",
essentials_tuple)
