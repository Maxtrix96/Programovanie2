from random import randrange

zoznam = [randrange(10, 100) for _ in range(20)]
print(zoznam)

def bubblesort(p):
    for i in range(len(p) - 1):
        vymena = False
        for j in range(len(p) - 1 - i):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]
                vymena = True
        
        if not vymena:
            break

    return p

print(bubblesort(zoznam))

def shakerSort(p):
    # bubblesort z oboch stran
    for i in range(len(p) - 1):
        vymena = False
        for j in range(len(p) - 1 - i):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]
                vymena = True
        
        if not vymena:
            break

    return p