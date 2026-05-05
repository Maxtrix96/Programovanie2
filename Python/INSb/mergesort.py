def mergesort(p:list[float]) -> list[float]:
    # baza rekurzie
    if len(p) < 2:
        return p # uz je usproiadane

    # rozdelenie (na mensie podproblemy)
    stred:int = len(p) // 2
    lava:list[float] = p[0:stred]
    prava:list[float] = p[stred:]

    # panuj (ries mensie podproblemy)

    lava_usp:list[float] = mergesort(lava)
    prava_usp:list[float] = mergesort(prava)

    # zlucenie (vytvorenie riesenia z rieseni podproblemov)

    vysl:list[float] = []

    while lava_usp and prava_usp:
        if lava_usp[0] < prava_usp[0]: # vyber prvy prvok zo zoznamu
            vysl.append(lava_usp.pop(0)) 
        else:
            vysl.append(prava_usp.pop(0))


    vysl.extend(lava_usp)
    vysl.extend(prava_usp)

    return vysl


from random import randrange

n = 20

arr = [randrange(n) for _ in range(n)]

print(arr)

print(mergesort(arr))