import requests
import json

auth = {'Authorization':'TOKEN'}

# get list of replay urls
with open('output.json') as f:
    data = json.load(f)
urls = [data["list"][j]["link"] for j in range(len(data["list"]))]
ids = [data["list"][j]["id"] for j in range(len(data["list"]))]

# download replay data
for i in range(len(urls)):
    r = requests.get(urls[i], headers=auth)
    with open(str(ids[i]) + '.json', 'w') as outfile:
        json.dump(r.json(), outfile)