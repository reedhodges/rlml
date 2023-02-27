import json

# import the json file
with open('output.json') as f:
    data = json.load(f)

# get all the values of the 'link' key from output.json
urls = [data["list"][j]["link"] for j in range(len(data["list"]))]
print(urls)