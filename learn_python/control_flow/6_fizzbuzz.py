i = 1
fizz_number = 3
buzz_number = 5

def check_multiple(check_number_1, check_number_2):
    return check_number_1 % check_number_2 == 0

while i < 101:
    if check_multiple(i, fizz_number) and check_multiple(i, buzz_number):
        print("FizzBuzz")
    elif check_multiple(i, fizz_number):
        print("Fizz")
    elif check_multiple(i, buzz_number):
        print("Buzz")
    else:
        print(i)
    i += 1