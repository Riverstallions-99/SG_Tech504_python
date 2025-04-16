# --- Start of Task "Python variable basics" ---
# A variable is a stored item of data assigned to a value
# A variable is called a variable because it can take many forms and can be changed; it is literally variable


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


# print("Please input your name: ")
# name = input()


name = input("Please input your name: ")
age = input("Please input your age(years): ")
user_DoB = input("Please input your date of birth(dd-mm-yyyy): ")

print("Hi " + name + ",",
      "You are " + age + " years old and your birthday is",
      user_DoB)

# --- End of Task "Python variable basics" ---