MEM = [None] * 1000
MEM[:1] = 0, 1

def fib_mem(n):
    if "count" not in dir(fib_mem):
        fib_mem.count = 0
    fib_mem.count +=1

    if MEM[n] is None:
        MEM[n] = fib_mem(n-1) + fib_mem(n-2)

    return MEM[n]
    
fib_mem(10)