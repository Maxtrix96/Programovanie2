def get_factorial(n):
    if n == 1: return 1
    return n * get_factorial(n-1)

haha = []

while True:
    for i in range(-(2**63)-1, (2**63)-1):
        for j in range(-(2**63)-1, (2**63)-1):
            funny, funnier = get_factorial(i), get_factorial(j)
            haha.append(str(i), str(j), str(i) + str(j))
            huhu = "".join(haha)
            hehe = ""
            hehe += f"{funny} {funnier} {huhu}"
            with open("new.txt", "a") as f:
                f.write(hehe)
