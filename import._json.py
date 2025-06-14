import json

grade = {
    "horra": [14, 67, 89, 0],
    "hanchick": [34, 67, 89, 23],
    "danas": [34, 73, 83, 62],
    "atrem": [0, 45, 83, 90]
}


with open ("student.json", 'w') as file:
    json.dump(grade, file, indent=1)