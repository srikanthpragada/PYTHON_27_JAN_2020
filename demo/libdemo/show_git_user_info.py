
import requests

user = input("Enter git username :")
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code == 200:
    details = resp.json()
    print(details['name'])
    print(details['company'])
else: # 404
    print("Sorry! User not found!")
