# Tuple
'''
Ordered: Tuples are part of sequence data types, which means they hold the order of the data insertion. It maintains the index value for each item.
Immutable: Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation.
Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
Duplicates: Tuples can contain duplicates, which means they can have items with the same value.
'''
Tuple = ('Aladdin',)
my_tuple = (10, 20, 30, 40, 50, 10)

# Finding the index of the element
my_tuple.index(30) # index() accepts 3 arguments: item, optionals(start, stop)
50 in my_tuple # Returns boolean

# Modifying Tuple by typecasting
# tuple to list > list to tuple

# Counting element occurence 
my_tuple.count() # method accepts one value and returns the number of time it appears.

# Deleting tuple
del my_tuple

# We can use sum(), chain(), and + to concatenate multiple tuples
# Tuple supports packing and unpacking

# Maximum, Minimum, All, Any
my_tuple.max() # Returns maximum numbers
my_tuple.min() # Returns minimum numbers
my_tuple.all() # Returns True if all value is > 0 | []
my_tuple.any() # Returns if any value is True
