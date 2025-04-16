# --- Start of Task "Use string methods" ---

str_with_extra_spaces = " extra spaces at the start and end "

# Write comment to explain what this does

print(len(str_with_extra_spaces)) # This will print the length of the string, which is 35

# Write comment to explain what this does

print(len(str_with_extra_spaces.strip())) # the strip method returns a trimmed version of the string, removing any
# leading or trailing whitespaces

# print(str_with_extra_spaces.strip())


example_text = "here's some text with some words of text"

# count how many times the substring 'text' occurs within example_text & print it to the screen
print(example_text.count("text"))

# convert example_text to lowercase & print it to the screen
print(example_text.lower())

# convert example_text to uppercase & print it to the screen
print(example_text.upper())

# capitalise the first letter in example_text & print it to the screen
print(example_text.capitalize())

# replace the word 'with' in example_text with a comma (,) instead & print it to the screen
print(example_text.replace(" with", ","))


# --- End of Task "Use string methods" ---