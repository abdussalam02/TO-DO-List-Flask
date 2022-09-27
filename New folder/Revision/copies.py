# Shallow and Deep Copy
import copy
a = [[2 , 8, 6],[9 , 58, 45]]
b = copy.deepcopy(a)
b[1][1] = 6
print(b)
print(a)