import os
import yaml

def check_valid_yaml_file(file_to_validate) -> bool:
    # check file exists
    if os.path.exists(file_to_validate): # returns the value of the second argument as the first is this file, the script you are trying to run
        # open file for reading
        file = open(file_to_validate, "r")
        # parse the YAML file - if it loads then the file contains valid YAML
        try:
            yaml.safe_load(file)
            file.close()
            print(f"{file_to_validate} is valid YAML!")
            return True
        except:
            print(f"{file_to_validate} is not valid YAML!")
            return False
    else:
        # alert user that file specified does not exist
        print("ERROR: File '" + file_to_validate + "' not found")
        return False

def check_valid_yaml(yaml_string_to_validate) -> bool:
    try:
        yaml.safe_load(yaml_string_to_validate)
        print("YAML string is valid!")
        return True
    except:
        print("YAML string is not valid!")
        return False