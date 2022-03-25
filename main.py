import requests

import json

import os
from os.path import join, dirname
from dotenv import load_dotenv


load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
API_URL = os.environ.get("API_URL")

response = requests.get(f"{API_URL}/my-list/all")

json_data = response.json()

mylist_url_list = []

for data in json_data:
    mylist_url_list.append(data["d_anime_store_url"])

for mylist_url in mylist_url_list:
    payload = {"url": mylist_url}
    r = requests.put(f"{API_URL}/my-list", data=json.dumps(payload))
    print(mylist_url)
    print(r.status_code)

print("All done! ✨ 🍰 ✨")