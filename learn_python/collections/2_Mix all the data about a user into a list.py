
name = input("Please input your name: ")
age = input("Please input your age(years): ")
user_DoB = input("Please input your date of birth(dd-mm-yyyy): ")
height_cm = input("Please input your height in cm: ")

print("Hi " + name + ",",
      "You are " + age + " years old and your birthday is",
      user_DoB)

user_details_list = [
      name,
      int(age),
      user_DoB,
      float(height_cm)
]

print(user_details_list)

print(type(user_details_list[1]))
print(user_details_list[3])