import requests
import json


# Make API Call and store responce
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
req = requests.get(url)
print(f"Status code: {req.status_code}")


# Explore the structure of the responce data
responce_dict = req.json()
readable_file = "data/readable_hn_data.json"
# secure file opening
with open(readable_file, "w") as f:
    json.dump(responce_dict, f, indent=4)
