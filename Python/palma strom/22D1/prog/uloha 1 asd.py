MEM = [None] * 1000
MEM[:1] = 0, 1
def fib_mem(n):
    if "count" not in dir(fib_mem):
        fib_mem.count = 0
    fib_mem.count +=1

    if MEM[n] is None:
        MEM[n] = fib_mem(n-1) + fib_mem(n-2)

    return MEM[n]

def fib_rek(n):
    if "count" not in dir(fib_rek):
        fib_rek.count = 0
    fib_rek.count +=1
    if n < 2:
        return n
    
    return fib_rek(n-1) + fib_rek(n-2)

skuska = "2\n5\n10"
spracovane = list(map(int, skuska.split("\n")))

for num in spracovane[1:]:
    fib_mem(num)
    fib_rek(num)
    print(fib_rek.count - fib_mem.count)
    fib_rek.count, fib_mem.count = 0, 0
