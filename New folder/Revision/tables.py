# outer loop
print("-" *48)
for i in range(1, 11):
    for j in range(1, 11):
        x = i*j
        if x < 10:
            x = "0" + str(x)
            print(x, end = " | ")
        elif x > 99:
            print(x, end= "|")
        else:
            print(x, end= " | ")
    print(" ")
print("-" *48)