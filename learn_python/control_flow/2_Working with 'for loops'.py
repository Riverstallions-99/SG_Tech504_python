list_data = [1, 2, 3, 4, 5]
embedded_lists = [
    [1,2,3],
    [4,5,6]
]
dict_data = {
    1: {
        "name": "Bronson",
        "money": "$0.05"},
    2: {
        "name": "Masha",
        "money": "$3.66"},
    3: {
        "name": "Roscoe",
        "money": "$1.14"}
}

for num in list_data:
    print(num * 2)

print("\n")

for item in embedded_lists:
    print(item)

print("\n")

for item in embedded_lists:
    print(item)
    for subitem in item:
        print(subitem)

print("\n")

for key in dict_data:
    print(key)

print("\n")

for value in dict_data.values():
        print(value)

print("\n")

for value in dict_data.values():
    for sub_value in value
- ￼￼Research changing file permissions￼￼￼￼￼￼￼￼  .values():
        print(sub_value)

print("\n")

for value in dict_data.values():
    print(value.get("money"))

print("\n")

for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found three")
    else:
        print("greater than 3")