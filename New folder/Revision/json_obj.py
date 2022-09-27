'''
dump =
dumps = Python object to Json string
loads = Json strings to Python object
stringify = json object to json string
jsonify = converts csv file into JSON
parse = json string to json object
'''

import json
from jsonify import convert


a = '[{"name": "Aladdin"}, {"phone": 7977646886}, {"city": "Thane"}]'

# This will convert the python object into str 
m = json.dumps(a)

# This will convert the json object into python object (list)
n = json.loads(a)

# This will convert json string to json object
o = json.parse(a)

# This will convert json object to json string
p = json.stringify(o)

# This will convert the csv file into JSON type
z = convert.jsonify("filename")
print("Successful")
