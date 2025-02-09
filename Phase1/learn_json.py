import json

person = {"name": "小李", "age": 25}
json_string = json.dumps(person)
print(json_string)