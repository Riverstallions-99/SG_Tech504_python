# --- Start of Task "Concatenate these variables with different data types" ---

x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print(f"{x}{y} " + z) # When using multiple types of variables to concatenate strings, the compiler doesn't know how
# to handle it so we must use formatted strings in order to refer to the variable in the string, then concatenate z
# onto the end
print(str(x) + str(y) + z) # Is another method of doing this where we tell the code to treat x and y as strings

# --- End of Task "Concatenate these variables with different data types" ---