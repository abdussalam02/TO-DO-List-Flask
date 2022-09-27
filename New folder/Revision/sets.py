# Sets
'''
Unordered: The items in the set are unordered, unlike lists, i.e., it will not maintain the order in which the items are inserted. The items will be in a different order each time when we access the Set object. There will not be any index value assigned to each item in the set.
Immutable: Set items must be immutable. We cannot change the set items, i.e., We cannot modify the items’ value. But we can add or remove items to the Set. A set itself may be modified, but the elements contained in the set must be of an immutable type.
Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
Unique: There cannot be two items with the same value in the set.
'''

book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}

# Accessing item in Set
for book in book_set:
    print(book)
    
# Inserting elements
book_set.add('The God of Small Things') # To add single elements
book_set.update(['Atlas Shrugged', 'Ulysses']) # Update to add more than one item

# Removing Elements
book_set.remove("Harry Potter")
book_set.discard("Angels and Demons") # Removes without raising an error
book_set.pop() # Randomly removes an item
book_set.clear() # Removes all items

# Deleting Set
del book_set

# Set Operations
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# Union Operations 
vibgyor_colors = color_set.union(remaining_colors) # using union() method
vibgyor_colors = color_set | remaining_colors # using OR operator

# Intersection Operations
new_set = color_set.intersection(remaining_colors) # using intersection() method
new_set = color_set & remaining_colors # using & Operator
color_set.intersection_update(remaining_colors) # updates the original set with common elements 

# Difference Operations
print(color_set - remaining_colors) # using '-' operator
print(color_set.difference(remaining_colors)) # using difference() method
color_set.difference_update(remaining_colors) # updates the original set with unique elements

# Symmetric Operations 
unique_items = color_set ^ remaining_colors # using '^' operator
unique_items2 = color_set.symmetric_difference(remaining_colors) # using symmetric_difference() method
color_set.symmetric_difference_update(remaining_colors) # updates the original set with unique elements from both

# Subset and Superset 
print(color_set2.issubset(color_set1)) # subset
print(color_set2.issuperset(color_set1)) # superset

# Disjoint
print(color_set2.isdisjoint(color_set1))

# Maximum, Minimum, Sum, All, Any
color_set.max() # Returns maximum numbers
color_set.min() # Returns minimum numbers
color_set.all() # Returns True if all value is > 0 | []
color_set.any() # Returns if any value is True

# Frozenset
# It is immutable in nature
# All other properties are similar to Set

rainbow = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
f_set = frozenset(rainbow)
