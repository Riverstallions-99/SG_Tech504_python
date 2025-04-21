story_1 = {
    'start': 'The Beginning',
    'middle': 'The Main Bit',
    'end': 'The Happy Ending'
}

print(story_1)
print(type(story_1))
print(story_1.keys())
print(story_1.values())
print(story_1.get('start'))
print(story_1.get('middle'))
print(story_1.get('end'))

story_1["character"] = "Susan"

print(f"The End. I hope you enjoyed the story about {story_1.get('character')}!" )