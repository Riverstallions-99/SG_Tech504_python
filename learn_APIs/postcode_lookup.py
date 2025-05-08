import requests
import json

json_body = json.dumps({'postcodes': ["NN9 6PU", "M6 6QA", "L8 4SB"]})
headers = {'Content-Type': 'application/json'}

postcodes_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

# print(postcodes_req.status_code)
# print(postcodes_req.json())

postcode_dictionary = json.loads(postcodes_req.text)
# print(postcode_dictionary.get("result"))


for item in postcode_dictionary.get("result"):
    for sub_item in item.get("result"):
        print(f"{sub_item}: {item.get('result').get(sub_item)}")
    print("\n")