import random
from random import randint
random.seed()

# Define/assign number to a variable called magic_number
magic_number = 42
num_guesses = 5
user_guess = 0
# first_guess = True
# success = False
# print(magic_number)

while num_guesses >= 1:
    user_guess = input(f"Please choose a number from 1 to 100 inclusive (You have {num_guesses} guesses left): ")
    if str(user_guess).isdigit() and 100 >= int(user_guess) > 0: # Check if the user has inputted a number
        if int(user_guess) == magic_number: # Check if the number is correct
            print("Well done! You guessed the correct number. Thank you for playing!")
            break
        elif int(user_guess) > magic_number:
            print("That was not the correct number, the magic number is lower than your guess.")
        else:
            print("That was not the correct number, the magic number is higher than your guess.")
        num_guesses -= 1
    else: # Catch that the user has not put in a number
        print("Your guess was not a valid number and will not be counted as a guess.")

