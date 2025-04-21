
# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# Define/assign number to a variable called magic_number
magic_number = 42

# Ask user for input
# Allow the user 5 guesses
num_guesses = 5
user_guess = 0
first_guess = True

while num_guesses >= 1:
    # Check if this input matches magic_number
    if int(user_guess) == magic_number:
        print("Well done! You guessed the right number.")
        break
    else: # Let the user know if the response was correct or not
        if not first_guess:
            print("That was not the correct number.")
        else:
            first_guess = False
        num_guesses -= 1
        user_guess = input(f"Please choose a number from 1 to 100 inclusive: ")

print("Thank you for playing")

