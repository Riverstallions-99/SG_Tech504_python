age = 0
# SET VARIABLE user_prompt TO TRUE
user_prompt = True
# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and (0 < int(age) <= 117):
        user_prompt = False
    else:
        print("Your input is not valid. Please try again.")
print(f"Your age is {age}")