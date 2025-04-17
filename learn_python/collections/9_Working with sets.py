# Sets are unordered, partially changeable
# Sets cannot have duplicate values
fruits = {
    "apple",
    "banana",
    "cherry"}

print(fruits)

fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.add("apple")
print(fruits)

# print(fruits[1])