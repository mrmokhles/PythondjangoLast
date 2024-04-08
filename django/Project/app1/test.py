import json

# a Python object (dict):
x=[
    {
        "id": 3,
        "name": "sadik",
        "email": "sadik@gmail.com",
        "bio": "student"
    },
    {
        "id": 4,
        "name": "farhan",
        "email": "farhan@gmail.com",
        "bio": "farmer"
    }
]

# convert into JSON:
y = json.dumps(x)

with open('C:/Users/doid/Desktop/django/jsonfile/data.json', 'w', encoding='utf-8') as f:
    json.dump(x, f, ensure_ascii=False, indent=4)
# the result is a JSON string:
print(y)