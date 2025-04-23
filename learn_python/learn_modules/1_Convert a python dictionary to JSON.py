import json
from validate_json_file import check_valid_json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# Using json.dumps which is useful for json strings specifically
# The 'indent=4' makes the output easier to read (4 is the length of a "tab")
servers_json = json.dumps(servers_dict, indent=4)

# Print the JSON-formatted string
print("JSON formatted data:")
print(servers_json)

# Write the JSON data to a file
# Using json.dump which is useful for writing to json files specifically
with open("servers.json", "w") as json_file:
    # Write the JSON string into the file
    json.dump(servers_dict, json_file, indent=4)

# Check if the made JSON file is valid JSON
check_valid_json("servers.json")