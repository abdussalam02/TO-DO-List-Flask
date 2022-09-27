# List
'''
Mutable: The elements of the list can be modified. We can add or remove items to the list after it has been created.
Ordered: Each item has a unique index value. 
Heterogenous: The list can contain different kinds of elements like string, integer, boolean, or any type.
Duplicates: The list can contain duplicates i.e., lists can have two items with the same values.
'''
# List methods for mutating elements
my_list = list([5, 8, 'Tom', 7.50])

# Accessing using index
my_list.index('Tom') # Returns the index of Tom
my_list[2] # Access the value at index 2

# Inserting methods
my_list.append(9) # appends at the end of the list
my_list.insert(3, 26) # uses index to insert the value insert(index, value)
my_list.extend([32, [25, 75, 100]]) # appends multiple elements or sublists
# Concatenation can be done with +

# To remove items
my_list.remove(26) # removes the first occurence
my_list.pop() # removes element using index if provided else the last element 

# To empty the list
my_list.clear() # Clears the list elements and returns an empty list

# To delete the list
del my_list # Deletes the list
del my_list[3:] # Deletes the sliced element only

# Sorting method
my_list.sort()

# Reversing a list
my_list.reverse()

# Maximum, Minimum, Sum, All, Any
my_list.max() # Returns maximum numbers
my_list.min() # Returns minimum numbers
my_list.sum() # Returns the sum of all elements
my_list.all() # Returns True if all value is > 0 | []
my_list.any() # Returns if any value is True


print(my_list)