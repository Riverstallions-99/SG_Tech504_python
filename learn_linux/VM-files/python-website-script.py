import sys, requests

url_to_use = sys.stdin.read()
full_url = f"https://{url_to_use}"
print(full_url)
print()
print(requests.get(full_url))
