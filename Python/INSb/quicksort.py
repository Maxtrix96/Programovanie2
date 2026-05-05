def quicksort(p):
    if len(p) <= 1:
        return p

    pivot = p[len(p) // 2]
    mensie = []
    rovne = []
    vacsie = []

    for item in p:
        if item < pivot:
            mensie.append(item)
        elif item == pivot:
            rovne.append(item)
        else:
            vacsie.append(item)
    
    return quicksort(mensie) + rovne + quicksort(vacsie)

from random import choice

def quicksortInak(p):
    if len(p) < 2:
        return p
    
    pivot = choice(p)
    mensie = [item for item in p if item < pivot]
    rovnake = [item for item in p if item == pivot]
    vacsie = [item for item in p if item > pivot]

    return quicksortInak(mensie) + rovnake + quicksortInak(vacsie)

from random import randrange

n = 20

arr = [randrange(n) for _ in range(n)]
arr2 = arr.copy()

print(arr)

print(quicksort(arr))

print(arr2)

print(quicksortInak(arr2))