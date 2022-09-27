# Dictionaries
'''
Unordered: The items in dictionaries are stored without any index value, which is typically a range of numbers. They are stored as Key-Value pairs, and the keys are their index, which will not be in any sequence.
Unique: As mentioned above, each value has a Key; the Keys in Dictionaries should be unique.  If we store any value with a Key that already exists, then the most recent value will replace the old value.
Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
Mutable: The dictionaries are collections that are changeable, which implies that we can add or remove items after the creation.
'''

person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# Accesing elements
print(person['name']) # raises keyerror if key not present 
print(person.get('telephone')) # raises None if key not present
print(person.keys()) # returns all keys present
print(person.values()) # returns all values present
print(person.items()) # returns all elements in key value pair

# Inserting elements
person["weight"] = 50 # assignment method
person.update({"height": 6}) # update() method to add multiple key:value pairs
person.update([("city", "Texas"), ("company", "Google",)])

# Removing elements
person.popitem() # Removes the last inserted item
person.pop('telephone') # Removes element using key
del person['weight'] # Deletes element in bracket
person.clear() # Removes all the elements 

# Deleting Dictionaries 
del person # Deletes the whole dictionary

# Adding dictionaries
dict1.update(dict2) # Joining 2 dictionaries
student_dict = {**student_dict1, **student_dict2, **student_dict3} # Joining multiple container
# If both the dictionaries have common keys, the value of first dictionary will be overriden with second


# Maximum, Minimum, Sum, All, Any
person.max() # Returns maximum numbers
person.min() # Returns minimum numbers
person.all() # Returns True if all value is > 0 | []
person.any() # Returns if any value is True