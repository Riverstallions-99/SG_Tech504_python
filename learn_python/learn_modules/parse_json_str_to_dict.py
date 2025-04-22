import json

# Load the JSON file
with open('servers.json', 'r') as json_file:
    # Load the JSON data from the file and pass to the loads() method as a string
    servers = json.loads(json_file.read())
# json.loads() method doesn't work when providing a file directly as it expects a string

# Confirm data type
print(type(servers))
# One way of printing the dictionary
print(servers.get("server1"))
# Another way of printing the dictionary
print(servers["server2"])

for key in servers.keys():
    print(f"\nKey and Value: '{key}' = '{servers.get(key)}'")
    for sub_key in servers.get(key).keys():
        print(f"Record key and sub value: '{sub_key}' = '{servers.get(key).get(sub_key)}'")