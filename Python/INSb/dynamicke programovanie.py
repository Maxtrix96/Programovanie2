iter = 20

vypocitane = [0, 1] + [None] * iter

def fibMemo(n):
    if vypocitane[n] is None:
        vypocitane[n] = fibMemo(n - 2) + fibMemo(n - 1)
    
    return vypocitane[n]

# print(fibMemo(iter))


def fibDP(n):
    FIB = [None] * (n+1)
    FIB[:2] = [0, 1]
    for i in range(2, n+1):
        FIB[i] = FIB[i - 1] + FIB[i-2]
    return FIB[n]

print([fibDP(i) for i in range (21)])

print(fibDP(100000))

def fibDP_pamat(n):
    # cas: O(n^2)
    # pamat: 3 premenne velkosti n bitov
    
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    
    return a


from functools import cache

@cache

def fib_cache(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    return fib_cache(n - 1) + fib_cache(n - 2)

