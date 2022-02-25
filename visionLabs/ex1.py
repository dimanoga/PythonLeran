import json

a1 = {'key': [3, 2, '1']}
b1 = {'key': [1, 2, 3]}

json_a = json.loads("""
                   {
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    }]  }        """)

json_b = json.loads("""
                   {
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    }] }         """)


json_c = json.loads("""
                   {
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29.00005,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    }]  }        """)



def sort_json(obj):
    if isinstance(obj, dict):
        return sorted((k, sort_json(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(sort_json(x) for x in obj)
    else:
        return obj


print(sort_json(a1) == sort_json(b1))

