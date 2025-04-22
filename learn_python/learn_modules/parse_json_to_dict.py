import json

# Open the JSON file
with open('servers.json', 'r') as json_file:
    # Load the JSON data from the file and convert it into a Python dictionary
    servers = json.load(json_file)

# print(type(servers)) # Confirm data type
print(servers.get("server1")) # One way of printing the dictionary
print(servers["server2"]) # Another way of printing the dictionary

for key in servers.keys():
    print(f"\nKey and Value: '{key}' = '{servers.get(key)}'")
    for sub_key in servers.get(key).keys():
        print(f"Record key and sub value: '{sub_key}' = '{servers.get(key).get(sub_key)}'")
