import os
import json

def check_valid_json(file_to_validate) -> bool:
    # check file exists
    if os.path.exists(file_to_validate): # returns the value of the second argument as the first is this file, the script you are trying to run
        # open file for reading
        file = open(file_to_validate, "r")
        try:
            # parse the JSON file - if it loads then the file contains valid JSON
            json.load(file)
            file.close()
            print("JSON file is valid!")
            return True
        except:
            print(f"{file_to_validate} is not valid JSON!")
            return False
    else:
        # alert user that file specified does not exist
        print("ERROR: File '" + file_to_validate + "' not found")
        return False
