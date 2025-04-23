import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the source file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()

        # Convert the YAML to JSON
        converted_json_content = json.dumps(source_content, sort_keys = False, indent = 4)

        # 2.1 Check the target file name was specified as an argument, if not, output the JSON to the screen instead
        # If there are 3 arguments (script to run, file to use, file to save to)
        if len(sys.argv) == 3:
            # 2.2 Check the target file doesn't already exist
            if os.path.exists(sys.argv[2]):
               print("ERROR: " + sys.argv[2] + " already exists, please delete file before trying again.")
            # 2.3 If previous conditions not met, then save JSON file
            else:
                # Save the JSON into a new file with the name for it received as an argument
                with open(sys.argv[2], "w") as json_file:
                    json_file.write(converted_json_content)
        # "if not, output the JSON to the screen instead"
        else:
            print(converted_json_content)
    # Condition: File not found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# Condition: No source file specified
else:
    print("ERROR: No YAML file was specified")
    print("Usage: yaml_to_json.py <source_file.yaml> <target_file.json>")