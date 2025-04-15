# --- Start of Task "Python variable basics" ---
'''
number_1 = 5
decimal_1 = 2.2
string_1 = "This is a string "

# == checks whether two values are equal, rather than assigning a value to that variable
if number_1 == 5:
    print("number is 5")

print(number_1)
print(decimal_1)
print(string_1)

# A strongly typed language is one that is strict on defining data types for variables, a weakly typed language can
# interpret the data type from the value, it is not specifically defined in the code
# Python is a weakly typed language, this can be shown here:
number_2 = 6
string_2 = "four"
# print (number2 + string2)
# The code above will result in a "TypeError" when run


# A dynamically typed language is one that determines variable types at runtime so there is no need to declare
# variable types, a statically typed language is one that requires the code to define the variable type before the
# code compiles. This means that in a dynamically typed language variables can change type mid-code.
# Python is a dynamically typed language
variable_1 = 1
print(variable_1)
variable_1 = "One"
print(variable_1)

print(id(number_1))
number_1 = 10
print(id(number_1))

# The id of the variable changes because the location of the value of the variable changes


x = 10
y = x

print(id(x))
print(id(y))
# The id of the variables is the same because they are essentially the same value, therefore python
# uses a reference to the same location to save data

x = 11
print(id(y))
# the id of y has stayed the same

# ---
# print("Please input your name: ")
# name = input()
# ---

name = input("Please input your name: ")
age = input("Please input your age(years): ")
user_DoB = input("Please input your date of birth(dd-mm-yyyy): ")

print("Hi " + name + ",",
      "You are " + age + " years old and your birthday is",
      user_DoB)
# --- End of Task "Python variable basics" ---
# --- Start of Task "Understand Operators" ---

x = 5
y = 1

z = x + y
a = y * 2
b = x / a
c = x % a

print(x, y, z, a, b, c)

if x > y:
    print("x is bigger than y")

if a < b:
    print("a is less than b")

if a == 2:
    print("y is equal to 2")

if c != 2:
    print("c is not equal to 2")

if b >= 2:
    print("b is greater than or equal to 2")

if z <= 7:
    print("z is less than or equal to 7")


# --- End of Task "Understand Operators" ---
# --- Start of Task "Create strings and use quotes appropriately" ---
#bad_string = 'I said 'Wow!''
#print(bad_string)

# This code fails as the compiler cannot tell where the string ends

good_string = 'I said "Wow!"'
print(good_string)

alt_good_string = "I said \"Wow!\""
print(alt_good_string)

more_alt_good_string = "I said 'Wow!'"
print(more_alt_good_string)

# When using quotes around strings in python, it's best to default to using one over another. This is outlined in PEP8.

# --- End of Task "Create strings and use quotes appropriately" ---
# --- Start of Task "Slice strings" ---

# Slicing strings is where you split up a string using array concepts, the code will treat the string as an array of
# characters and you can refer to each character using an integer

Hw = "Hello world!"
print(Hw)

print(len(Hw)) # 12

print(Hw[0]) # H

print(Hw[len(Hw) - 1]) # !
# Using this method ensures that even if the string changes, the code here doesn't need to be altered

print(Hw[len(Hw) - 2]) # d

print(Hw[2:]) # llo world!
# This code will take the 3rd value in the string (zero indexed array)

print(Hw[-3:]) # ld!
# This code will ask similarly to above except it will "start" at the end of the string, -3 refers to the 3rd character
# from the end backwards

print(Hw[:5]) # Hello (without space at the end)
# This code will print from the beginning up to the 5th character in the string

print(Hw[1:4]) # ell
'''
# --- End of Task "Slice strings" ---
# --- Start of Task "Finish the guessing game with string slicing" ---

# Guess the word with 4 hints to help
# Rationale: Practice word slicing
# Type of exercise: Finish the code

original_word = "recommendation"
scrambled_word = "eoommandretnic"

# Create the hint slices...
# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed
hint1_slice = original_word[4:6]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed
hint2_slice = original_word[-3:]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed
hint3_slice = original_word[7:10]

# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]". Use the hints below to know what slice is needed
hint4_slice = original_word[:2]

# Game instructions

print("Scrambled word:", scrambled_word)
print("Guess the original word from the scrambled version.")
print("Here are some hints:")

# Hints based on list slicing

print("Hint 1: The 5th and 6th letters are '" + hint1_slice + "'.")
print("Hint 2: The last 3 letters are '" + hint2_slice + "'.")
print("Hint 3: The 8th to 10th letters are '" + hint3_slice + "'.")
print("Hint 4: The first two letters are '" + hint4_slice + "'.")

# Game ends here

print("What's your guess?")
