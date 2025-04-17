frozen_set = frozenset([
    "hello",
    "world"
])
frozenset(frozen_set)
#frozen_set.add("!")

normal_set = {
    "let's",
    "learn"
}
print(normal_set)

normal_set.update(frozen_set)
print(normal_set)

