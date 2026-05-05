from random import randrange

zoznam = [randrange(10, 100) for _ in range(20)]
print(zoznam)

def selectionSort(p):
    # O(n^2)
    for i in range(len(p) - 1):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
    
    return p

print(selectionSort(zoznam))