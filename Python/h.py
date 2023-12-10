x = int(input("zadaj x"))
y = int(input("zadaj y"))

for i in range(x):
    print(i+1, ": ", end=" ")
    for j in range(y):
        print((i+1)*(j+1), end=" ")
    print(" ")
