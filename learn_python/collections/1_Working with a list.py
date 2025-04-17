shopping_list = ["eggs",
                 "bread",
                 "bananas",
                 "biscuits",
                 "milk"]

print(shopping_list)
print(type(shopping_list))

print(shopping_list[0])
print(shopping_list[-1])

shopping_list[1] = "rice"
print(shopping_list[1])

shopping_list.append("carrots")
print(shopping_list)
print(len(shopping_list))

shopping_list.extend(["toffee", "coffee"])
print(shopping_list)

shopping_list.remove("bananas")
print(shopping_list)

shopping_list.pop()
print(shopping_list)