maxPostupnost = []
maxSucet = 0
karty = [100, 1, 1, 1, 99, 98, 97] # [1, 3, 1, 5, 2]
zoznam = [None] * len(karty)
pocetKombinacii = 0

def spracuj():
    global maxSucet
    global maxPostupnost
    global pocetKombinacii
    pocetKombinacii += 1

    sucet = 0
    leftIdx = 0
    rightIdx = len(karty) - 1
    for i in range(len(zoznam)):
        if (zoznam[i]) == 0:
            sucet += karty[leftIdx] * (i + 1)
            leftIdx += 1
        else:
            sucet += karty[rightIdx] * (i + 1)
            rightIdx -= 1
    
    print(f'{zoznam} {sucet}')

    if sucet > maxSucet:
        maxSucet = sucet
        maxPostupnost = zoznam.copy()


def generuj(odIdx):
    if odIdx == len(zoznam):
        spracuj()
        return
    
    for i in range(2):
        zoznam[odIdx] = i
        generuj(odIdx + 1)
    
generuj(0)

print(f"postupnost: {maxPostupnost}, jej sucet sucinov: {maxSucet}")
print(f"pocet kombinacii: {pocetKombinacii}")