# Python script needs to accept an argument specify the website you want to get the HTML for & print it to the screen

import sys, requests

url_to_use = sys.stdin.read()

print(requests.get(f"https://{url_to_use}"))
