# --- MVP ---
def addition(a:int, b:int) -> int:
    return a + b

def subtraction(a:int, b:int) -> float:
    return a - b

def multiplication(a:int, b:int) -> int:
    return a * b

def division(a:int, b:int) -> float:
    return a / b


first_digit = int(input("Please input your first number: "))
second_digit = int(input("Please input your second number: "))
operator = input("Please input your operator ( +, -, *, /): ")

if operator == "+":
    print(addition(first_digit, second_digit))
elif operator == "-":
    print(subtraction(first_digit, second_digit))
elif operator == "*":
    print(multiplication(first_digit, second_digit))
elif operator == "/":
    print(division(first_digit, second_digit))
else:
    print("You have not entered a valid option")