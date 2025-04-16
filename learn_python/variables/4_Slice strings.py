# --- Start of Task "Slice strings" ---

# Slicing strings is where you split up a string using array concepts, the code will treat the string as an array of
# characters, and you can refer to each character using an integer

Hw = "Hello world!"
print(Hw)

print(len(Hw)) # OUTPUT 12

print(Hw[0]) # OUTPUT H

print(Hw[len(Hw) - 1]) # OUTPUT !
# Using this method ensures that even if the string changes, the code here doesn't need to be altered

print(Hw[len(Hw) - 2]) # OUTPUT d

print(Hw[2:]) # OUTPUT llo world!
# This code will print the string from the 3rd value (zero indexed array)

print(Hw[-3:]) # OUTPUT ld!
# This code will print similarly to above except it will "start" at the end of the string and count backwards,
# -3 refers to the 3rd character from the end

print(Hw[:5]) # OUTPUT Hello (without space at the end)
# This code will print from the beginning up to the 5th character in the string

print(Hw[1:4]) # OUTPUT ell

# --- End of Task "Slice strings" ---