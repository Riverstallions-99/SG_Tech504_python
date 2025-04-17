input_string = "Hello again!"

def print_something(input_string_argument):
    print(input_string_argument)

print_something(input_string)

# ---

def greet(name):
    print("Hello, my name is " + name + ".")

greet("Susan")

# ---

def addition(int1, int2):
    return int1 + int2 # must include return

value = addition(2, 2)
# print(addition(2, 2))

# --- Task 6

def addition(int1 = 2, int2 = 2):
    return int1 + int2 # must include return

print(addition())
print(addition(4, 4)) # the function has added 4 and 4 which makes 8, the default values have been overwritten


def print_every_number(numbers_tuple): # When using the *, the question is not answered
    print(type(numbers_tuple))
    for i in numbers_tuple:
        print(i)

print_every_number((1, 2, 2, 3, 3, 4, 5, 5))

# --- Task 7

# greet(24601) # The code does not like being given an int when the function is treating the argument as a string

def print_something(input_string_new: str):
    print(input_string_new)

def division(x:int = 2, y:int = 5) -> float:
    return x / y

a:int = 4
b:int = 6
print(division(a, b))
print(division())