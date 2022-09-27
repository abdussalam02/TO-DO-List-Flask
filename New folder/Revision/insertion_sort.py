# Insertion Sort
a = [4, 9, 6, 54, 87, 1, 3, 5]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)