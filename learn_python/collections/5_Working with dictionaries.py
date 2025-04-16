student_1 = {'name': 'susan',
             'stream': 'tech',
             'completed_lessons': int(4),
             'completed_lesson_names': ["variables", "data_types", "set up"]
             }

# A set of key:value pairs, the key must always be a string or int or an immutable type (such as a tuple, as long as the tuple doesn't contain a mutable value itself
# The key becomes a pointer for the value, therefore it cannot be changed after it is set (immutable)
print(student_1)
print(type(student_1))
print(student_1.get("stream"))
print(student_1.get("completed_lesson_names"))

student_1['completed_lessons'] = int(3)
print(student_1)

# First pass
completed_lesson_names_list = student_1['completed_lesson_names']
# ^ Grabs the list of completed lesson names and puts them in a list
completed_lesson_names_list.remove("data_types")
# ^ Removes the "data_types" value from the list
student_1["completed_lesson_names"] = completed_lesson_names_list
# ^ Updates the completed lesson names with the list we just made and updated

student_1['completed_lessons'] = int(len(student_1['completed_lesson_names']))
# ^ Updates the number of completed lessons, for my peace of mind
print(student_1)


# Second pass once removing redundant code (3 lines of code into 1)
student_1["completed_lesson_names"] = (student_1['completed_lesson_names']).remove("data_types")
# ^ Removes the "data_types" value from the list which is in the value for the key "completed_lesson_names"

student_1['completed_lessons'] = int(len(student_1['completed_lesson_names']))
# ^ Updates the value for the number of lessons completed, otherwise it would just be wrong and I couldn't leave it wrong

print(student_1.keys())