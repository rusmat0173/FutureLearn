""" Practice of week 2 JSON stuff on this course """

# import Python's JSON library.
# JSON is similar to Python dictionary format
import json
import requests     # <=had to import this into PyCharm, for this Project

# below in JSON structure
my_data = {
    "name": "Rusmat",
    "favourite number": 7,
    "hobbies": ["Python, X-Trainer"]
}

with open("rusmat.json", "w") as f:
    json.dump(my_data, f)

# when you inspect rusmat.json, you see it stores the 3 types of variables, ot just all as strings like a csv file!!!

# now just reading it is quite simple:
with open("rusmat.json", "r") as f:
    data2 = json.load(f)
    print(data2)

for info in data2:
    print(info)

print(data2.values())
print("+ + + + + + +")

# json as API to websites
r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
NASA = r.json()
print(NASA)



