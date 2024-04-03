



def fib_rek(n):
    if "count" not in dir(fib_rek):
        fib_rek.count = 0
    fib_rek.count += 1
    if n < 2:
        return n
    
    return fib_rek(n-1) + fib_rek(n-2)

print(fib_rek(10))


def fib_rek(n):
    if "count" not in dir(fib_rek):
        fib_rek.count = 0
    fib_rek.count += 1
    if n < 2:
        return n
    
    return fib_rek(n-1) + fib_rek(n-2)

