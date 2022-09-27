# Number to Even Odd
a = [2, 7, 5, 8, 1, 6]
b = []
for i in a:
    if i % 2 == 0:
        b.append("even")
    else:
        b.append("odd")
            
print(b)

# List Comprehension
a = [2, 7, 5, 8, 1, 6]
b = ["Even" if i%2==0 else "Odd" for i in a]
print(b)

# Using Enumerate
a = [2, 7, 5, 8, 1, 6]

for i, v in enumerate(a):
    if v % 2 == 0:
        a[i] = "Even"
    else:
        a[i] = "Odd"
        
print(a)

# using function and map
a = [2, 7, 5, 8, 1, 6]
def fun(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"

b = list(map(fun, a))
b

# Using map and lambda
a = [2, 7, 5, 8, 1, 6]
b = list(map(lambda a: "Even" if a%2==0 else "Odd", a))
print(b)

