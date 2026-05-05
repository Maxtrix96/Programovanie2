from random import randrange

zoznam = [randrange(10, 100) for _ in range(20)]
print(zoznam)

def insertsort(p):
    # O(n^2)
    for idx in range(1, len(p) - 1):
        # vloz prvok p[idx] na spravnu poziciu; posuvaj dolava
        j = idx - 1
        while j >= 0 and zoznam[j] > zoznam[j + 1]: # kym nie su na zaciatku a su v zlom poradi
            zoznam[j], zoznam[j + 1] = zoznam[j + 1], zoznam[j]
            j -= 1

        print(zoznam[:idx + 1], end=" ")
        if idx < len(zoznam) - 1:
            print('|', zoznam[idx + 1])
        else:
            print()

insertsort(zoznam)


