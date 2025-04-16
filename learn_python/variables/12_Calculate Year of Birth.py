# Write a python script to calculate the user's year of birth

# · define the variables age_int and name_str (set dummy/default/initial values)
# · make a calculation for the year in which the person was born
# · print out "OMG , you are years old so you were born in " with the correct values
# ---
# · prompt the user for inputs and assign the variable age_int and name_str
# · remove the initial values set
# ---
# · calculate and print out the total number of hours this person has lived
# ---

import datetime
from datetime import timedelta, datetime

name_str = input("What is your name? ")
age_int = int(input("What is your age? "))

year = int(datetime.now().date().strftime("%Y")) - age_int
yearNow = datetime.now().year

print(f"OMG {name_str}, you are {age_int} years old so you were born in {year}")

hours = timedelta(days = year * 365) // 3600  # TODO finish


print(f"You have been alive for {hours} hours")